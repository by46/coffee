-- --------------------------------------------------------------------------------
-- Routine DDL
-- --------------------------------------------------------------------------------
DELIMITER $$

CREATE DEFINER=`root`@`%` PROCEDURE `new_user`(
OUT MSG VARCHAR(8)
)
BEGIN
    SET MSG='failure';
END
