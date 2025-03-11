-- 코드를 입력하세요
-- patient 환자, doctor 의사, appointment 예약목록
-- 2022-04-13 취소x(=예약된) 예약내역 조회
-- => 예약번호, 환자이름, 환자번호, 진료과코드, 의사이름, 진료예약일시(오름)
SELECT a.apnt_no, p.pt_name, p.pt_no, d.mcdp_cd, d.dr_name, a.apnt_ymd
FROM appointment a
JOIN patient p ON a.pt_no = p.pt_no
JOIN doctor d ON a.mddr_id = d.dr_id
WHERE a.apnt_ymd LIKE '2022-04-13%' AND a.apnt_cncl_yn = 'N'
ORDER BY a.apnt_ymd