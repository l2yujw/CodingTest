-- 코드를 입력하세요
-- used_goods_board 게시판 정보
-- used_goods_file 첨부파일 정보
-- 조회수 가장 많의 첨부파일 경로, file_id(내림)
-- 기본 파일 경로 /home/grep/src/, 게시글 id 기준 디렉터리 구분
-- => 파일id, 파일 이름, 파일 확장자
SELECT concat('/home/grep/src/', board_id, '/', file_id, file_name, file_ext) as file_path
FROM used_goods_file
WHERE board_id = (SELECT board_id
                 FROM used_goods_board
                 ORDER BY views desc
                 LIMIT 1)
ORDER BY file_id desc