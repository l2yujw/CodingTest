-- 코드를 입력하세요
-- memeber_profile 고객 정보
-- rest_review 리뷰정보
-- 리뷰를 가장 많이 작성한 회원의 리뷰들
SELECT p.member_name, r.review_text, date_format(r.review_date, '%Y-%m-%d') as review_date
FROM rest_review r
JOIN member_profile p ON r.member_id = p.member_id
WHERE r.member_id = (SELECT member_id
                     FROM rest_review
                     GROUP BY member_id
                     ORDER BY count(member_id) desc
                     LIMIT 1)
ORDER BY review_date, review_text