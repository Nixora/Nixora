src=open('enterprise-ai-platform.html','r',encoding='utf-8').read()
r=[('<title>Enterprise AI Platform','<title>Identity and Access Management Services'),('href="enterprise-ai-platform.html" class="mega-link active-mega-link">Enterprise AI Platform','href="enterprise-ai-platform.html" class="mega-link">Enterprise AI Platform'),('href="service.html" class="mega-link">Identity and Access Management Services','href="identity-access-management-services.html" class="mega-link active-mega-link">Identity and Access Management Services')]
for o,n in r: src=src.replace(o,n)
open('identity-access-management-services.html','w',encoding='utf-8').write(src)
print('done',len(src))
