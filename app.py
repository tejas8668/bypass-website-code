from flask import Flask, render_template, request, jsonify, session
import cloudscraper
from bs4 import BeautifulSoup
import time
import os
import random
from login import token_required, init_login_routes

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', os.urandom(24))  # For session management

# Initialize login routes
init_login_routes(app)

# Store active sessions
active_sessions = {}

# List of free proxies (you can update this list with working proxies)
FREE_PROXIES = [
    # Format: 'http://ip:port'
    # Leave empty for now, update with working proxies as needed
]

def get_random_proxy():
    if FREE_PROXIES:
        return random.choice(FREE_PROXIES)
    return None

'''def Seturl_in(url, retry=False):
    client = cloudscraper.create_scraper(allow_brotli=False)
    DOMAIN = "https://set.seturl.in/"
    url = url[:-1] if url[-1] == "/" else url
    code = url.split("/")[-1]
    final_url = f"{DOMAIN}/{code}"
    ref = "https://loan.creditsgoal.com/"
    h = {"referer": ref}
    
    try:
        resp = client.get(final_url, headers=h)
        soup = BeautifulSoup(resp.content, "html.parser")
        inputs = soup.find_all("input")
        data = {input.get("name"): input.get("value") for input in inputs}
        h = {"x-requested-with": "XMLHttpRequest"}
        time.sleep(7)
        r = client.post(f"{DOMAIN}/links/go", data=data, headers=h)
        return str(r.json()["url"])
    except BaseException as e:
        if not retry:
            print(f"Error occurred: {e}. Retrying...")
            return Seturl_in(url, retry=True)
        else:
            return "Something went wrong, Please Wait For Few Seconds and try again..."'''
        
def Seturl_in(url, retry=False, session_id=None):
    # Get or create session
    if retry and session_id and session_id in active_sessions:
        client = active_sessions[session_id]
    else:
        # Get a random proxy
        proxy = get_random_proxy()
        proxies = {"http": proxy, "https": proxy} if proxy else None
        
        # Enhanced cloudscraper configuration
        client = cloudscraper.create_scraper(
            browser={
                'browser': 'chrome',
                'platform': 'windows',
                'mobile': False
            },
            delay=10,
            allow_brotli=False,
            interpreter='js2py'
        )
        
        # Add common browser headers
        client.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'Cache-Control': 'max-age=0',
            'TE': 'Trailers'
        })
        
        # Set proxies if available
        if proxies:
            client.proxies = proxies
            
        if session_id:
            active_sessions[session_id] = client

    DOMAIN = "https://set.seturl.in/"
    url = url[:-1] if url[-1] == "/" else url
    code = url.split("/")[-1]
    final_url = f"{DOMAIN}/{code}"
    ref = "https://loan.creditsgoal.com/"
    h = {"referer": ref}
    
    try:
        # Try to get the page
        resp = client.get(final_url, headers=h)
        
        # Check if we got Cloudflare challenge
        if "Just a moment" in resp.text or "Enable JavaScript" in resp.text:
            return {
                "status": "cloudflare",
                "message": "Cloudflare detected. Please try again.",
                "session_id": session_id
            }
        
        # If we got past Cloudflare, process the response
        soup = BeautifulSoup(resp.content, "html.parser")
        inputs = soup.find_all("input")
        data = {input.get("name"): input.get("value") for input in inputs}
        h = {"x-requested-with": "XMLHttpRequest"}
        time.sleep(7)
        r = client.post(f"{DOMAIN}/links/go", data=data, headers=h)
        return {
            "status": "success",
            "url": str(r.json()["url"])
        }
        
    except BaseException as e:
        return {
            "status": "error",
            "message": str(e),
            "session_id": session_id
        }


def runurl(url, retry=False, session_id=None):
    # Get or create session
    if retry and session_id and session_id in active_sessions:
        client = active_sessions[session_id]
    else:
        # Get a random proxy
        proxy = get_random_proxy()
        proxies = {"http": proxy, "https": proxy} if proxy else None
        
        # Enhanced cloudscraper configuration
        client = cloudscraper.create_scraper(
            browser={
                'browser': 'chrome',
                'platform': 'windows',
                'mobile': False
            },
            delay=10,
            allow_brotli=False,
            interpreter='js2py'
        )
        
        # Add common browser headers
        client.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'Cache-Control': 'max-age=0',
            'TE': 'Trailers'
        })
        
        # Set proxies if available
        if proxies:
            client.proxies = proxies
            
        if session_id:
            active_sessions[session_id] = client

    DOMAIN = "https://get.runurl.in/"
    url = url[:-1] if url[-1] == "/" else url
    code = url.split("/")[-1]
    final_url = f"{DOMAIN}/{code}"
    ref = "https://learna1.bgmi32bitapk.in/"
    h = {"referer": ref}
    
    try:
        # Try to get the page
        resp = client.get(final_url, headers=h)
        
        # Check if we got Cloudflare challenge
        if "Just a moment" in resp.text or "Enable JavaScript" in resp.text:
            return {
                "status": "cloudflare",
                "message": "Cloudflare detected. Please try again.",
                "session_id": session_id
            }
        
        # If we got past Cloudflare, process the response
        soup = BeautifulSoup(resp.content, "html.parser")
        inputs = soup.find_all("input")
        data = {input.get("name"): input.get("value") for input in inputs}
        h = {"x-requested-with": "XMLHttpRequest"}
        time.sleep(7)
        r = client.post(f"{DOMAIN}/links/go", data=data, headers=h)
        return {
            "status": "success",
            "url": str(r.json()["url"])
        }
        
    except BaseException as e:
        return {
            "status": "error",
            "message": str(e),
            "session_id": session_id
        }

def process_url_with_retries(url, function, retry_count=3, session_id=None):
    """
    Process URL with automatic retries for Cloudflare protection
    """
    for attempt in range(retry_count):
        try:
            # Process URL with appropriate function
            result = function(url, retry=(attempt > 0), session_id=session_id)
            
            # If cloudflare is detected and we have more retries, try again
            if result.get('status') == 'cloudflare' and attempt < retry_count - 1:
                time.sleep(5)  # Wait before retry
                continue
                
            return result
            
        except Exception as e:
            if attempt < retry_count - 1:
                time.sleep(5)  # Wait before retry
                continue
            return {
                'status': 'error',
                'message': f'Error after {retry_count} attempts: {str(e)}',
                'session_id': session_id
            }

@app.route('/')
@token_required
def home():
    return render_template('index.html')

@app.route('/process_url', methods=['POST'])
@token_required
def process_url():
    url = request.form.get('url')
    retry = request.form.get('retry', 'false').lower() == 'true'
    session_id = request.form.get('session_id')
    
    if not url:
        return jsonify({'status': 'error', 'message': 'Please provide a URL'})
    
    # Generate a new session ID if not provided
    if not session_id:
        session_id = os.urandom(16).hex()
    
    # Check which domain the URL belongs to and process with retries if not explicitly retrying
    if "runurl.in" in url:
        if retry:
            result = runurl(url, retry, session_id)
        else:
            result = process_url_with_retries(url, runurl, retry_count=3, session_id=session_id)
    elif "seturl.in" in url:
        if retry:
            result = Seturl_in(url, retry, session_id)
        else:
            result = process_url_with_retries(url, Seturl_in, retry_count=3, session_id=session_id)
    else:
        return jsonify({'status': 'error', 'message': 'Unsupported URL. Only runurl.in and seturl.in are supported.'})
    
    # If no session ID in result, add it
    if result.get('status') in ['cloudflare', 'error'] and 'session_id' not in result:
        result['session_id'] = session_id
    
    return jsonify(result)

# Cleanup function for old sessions (can be run periodically)
def cleanup_old_sessions():
    # Implementation to remove old sessions if needed
    pass

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port) 