-- 코드를 입력하세요
-- memeber_profile 고객 정보
-- rest_review 리뷰정보
-- 리뷰를 가장 많이 작성한 회원의 리뷰들
WITH most_active_member AS (
    SELECT member_id
    FROM rest_review
    GROUP BY member_id
    ORDER BY COUNT(*) DESC
    LIMIT 1
)

SELECT p.member_name, r.review_text, DATE_FORMAT(r.review_date, '%Y-%m-%d') AS review_date
FROM rest_review r
JOIN member_profile p ON r.member_id = p.member_id
JOIN most_active_member m ON r.member_id = m.member_id
ORDER BY review_date, review_text;
