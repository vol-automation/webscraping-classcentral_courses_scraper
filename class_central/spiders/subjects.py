from logging import info
from scrapy import Spider
from scrapy.http import Request
import re

class SubjectsSpider(Spider):
    name = 'subjects'
    allowed_domains = ['class-central.com','classcentral.com']
    start_urls = ['http://class-central.com/subjects']

    def __init__(self, subject=None, filter=None):
        if subject != None:
            subject = subject.lower().strip()
            if subject in ['math','maths']:
                subject = "mathematics"
            if subject in ['human','humanity']:
                subject = "humanities"
            if subject in ['art','design','art and design']:
                subject = "art & design" 
            if subject in ['enginer']:
                subject = "Engineering" 
            if subject in ['health','medicine','health and medicine']:
                subject = "Health & Medicine"
            if subject in ['social']:
                subject = "Social Sciences"       
            if subject in ['education', 'teaching', 'education and teaching']:
                subject = "Education & Teaching"                                      
            subject = subject.title()               
        self.subject = subject
        self.filter = filter


    def parse(self, response):
       if self.subject:
           subject_url = response.xpath('//*[contains(@title,"{0}")]/@href'.format(self.subject)).extract_first()
           yield Request(url=response.urljoin(subject_url), callback=self.parse_subject)
       else:
           # fetch all subjects
           self.logger,info('%%%%%%%%%% Scraping all subjects %%%%%%%%%%')
           subjects = response.xpath('//section[contains(@class,"width-page")]/ul//h3/a[contains(@href,"/subject/")][1]/@href').extract()
           for subject in subjects:
               yield Request(response.urljoin(subject), callback=self.parse_subject)
           
    def parse_subject(self, response):
        subject_name = response.xpath('//title/text()').extract_first().split(' | ')[0].strip()
        
        subject_name_match = re.compile('\d+\+(.+)\[').search(subject_name)
        if subject_name_match is not None:
            subject_name = subject_name_match.group(subject_name_match.lastindex).strip() 
        
        # all courses
        courses = response.xpath('//span[@itemprop="name"]')
        
        if self.filter == 'free':
            courses = response.xpath('//span[@itemprop="name" and not(following-sibling::i)]')
            
        if self.filter == 'paid':
            courses = response.xpath('//span[@itemprop="name" and following-sibling::i]')            
        
        for course in courses:
            paid = course.xpath('./following-sibling::i[contains(@class,"icon-dollar")]') != []
             
            course_name = course.xpath('./text()').extract_first().strip()
            course_url = response.urljoin(course.xpath('./parent::a[1]/@href').extract_first())
            yield {
                'Subject': subject_name,
                'Course name': course_name,
                'URL' : course_url,
                'Paid?' : paid
            }
        next_page = response.urljoin(response.xpath('//*[@rel="next"]/@href').extract_first())
        yield Request(next_page, callback=self.parse_subject)
        
        
        
