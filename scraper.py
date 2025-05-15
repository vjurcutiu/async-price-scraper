import asyncio
import aiohttp
import async_timeout
import hashlib
import os
import json

# Simple file-based cache
CACHE_DIR = 'cache'
os.makedirs(CACHE_DIR, exist_ok=True)

async def fetch(session, url):
    # Generate cache key
    key = hashlib.md5(url.encode()).hexdigest()
    cache_path = os.path.join(CACHE_DIR, f"{key}.json")
    # Return cached response if recent
    if os.path.exists(cache_path):
        with open(cache_path) as f:
            return json.load(f)

    for attempt in range(3):
        try:
            async with async_timeout.timeout(10):
                async with session.get(url) as response:
                    text = await response.text()
                    # Basic parse: pretend JSON or wrap text
                    result = {'url': url, 'content': text}
                    # Cache the result
                    with open(cache_path, 'w') as f:
                        json.dump(result, f)
                    return result
        except Exception as e:
            await asyncio.sleep(2 ** attempt)
    return {'url': url, 'error': 'Failed after retries'}

async def scrape(urls):
    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, url) for url in urls]
        return await asyncio.gather(*tasks)

def generate_report(results, report_path='report.json'):
    # Simple report: count success, failures
    summary = {'total': len(results), 'failures': 0}
    for r in results:
        if 'error' in r:
            summary['failures'] += 1
    with open(report_path, 'w') as f:
        json.dump({'summary': summary, 'details': results}, f, indent=2)
    print(f"Report saved to {report_path}")

if __name__ == '__main__':
    # Example URLs list
    urls = [
        'https://httpbin.org/get?item=1',
        'https://httpbin.org/get?item=2',
        'https://httpbin.org/status/500',
    ]
    results = asyncio.run(scrape(urls))
    generate_report(results)
