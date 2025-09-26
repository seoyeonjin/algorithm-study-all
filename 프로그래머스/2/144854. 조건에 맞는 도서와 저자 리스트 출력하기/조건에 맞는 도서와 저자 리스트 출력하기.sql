-- 코드를 입력하세요
SELECT BOOK_ID, AUTHOR_NAME, DATE_FORMAT(PUBLISHED_DATE, '%Y-%m-%d') as PUBLISHED_DATE
from book as b 
LEFT JOIN author as a
on b.AUTHOR_ID = a.AUTHOR_ID
where category = '경제'
order by published_date;