import backendsContent from './backends.md';

addEventListener('fetch', event => {
  event.respondWith(handleRequest(event.request));
});

const backends = backendsContent.split('\n').filter(url => url.trim() !== '');

async function handleRequest(request) {
  // 随机选择一个后端服务器
  const backend = backends[Math.floor(Math.random() * backends.length)];
  
  // 构建新的请求 URL
  const url = new URL(request.url);
  url.hostname = new URL(backend).hostname;
  
  // 转发请求到选定的后端服务器
  const modifiedRequest = new Request(url, request);
  const response = await fetch(modifiedRequest);
  return response;
}
