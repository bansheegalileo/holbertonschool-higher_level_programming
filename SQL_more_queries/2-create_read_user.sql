-- Creates d8ab8se and user with select priv.
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER user_0d_2@localhost IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON hbtn_0d_2.* TO user_0d_2@localhost; 
 