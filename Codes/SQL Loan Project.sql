create database LoanProject

use LoanProject

select count(*) from account

select count(*) from card

select count(*) from client

select count(*) from disp

select count(*) from district

select count(*) from loan

select count(*) from [dbo].[order]

select count(*) from transaction_data

select * into loan_trans from
(select td.*, ln.loan_id, ln.date loan_date, ln.amount loan_amount,ln.duration loan_duration, ln.payments loan_payments,
ln.status loan_status from loan ln
join transaction_data td on ln.account_id = td.account_id)A

select * from [dbo].[loan_trans]

select * into acc_ord from 
(select o.*,acc.date account_date, acc.district_id as account_district_id, acc.frequency as account_frequency from account acc left join
[dbo].[order] o on acc.account_id = o.account_id)B

select * from [dbo].[acc_ord]

select * into card_disp from
(select card.*, disp.account_id disposition_account_id, disp.client_id as disposition_client_id,
disp.type as disposition_type from card card join
disp disp on card.disp_id = disp.disp_id)C

select * from [dbo].[card_disp]

select * into card_disp_client from 
(select * from card_disp cd join client c on cd.disposition_client_id = c.client_id)D

select * from card_disp_client

select * into card_disp_client_dist from 
(select * from card_disp_client cdc join district dist on cdc.district_id = dist.A1)E

select * from card_disp_client_dist

select * into acc_ord_card_disp_client_dist from
(select cdcd.*,ao.order_id,ao.bank_to,ao.account_to,ao.amount,ao.k_symbol,ao.account_date,ao.account_district_id,ao.account_frequency
from acc_ord ao left join card_disp_client_dist cdcd on ao.account_id = cdcd.disposition_account_id)F

select * from [dbo].[acc_ord_card_disp_client_dist]

select * from acc_ord_card_disp_client_dist aocdcd join loan_trans lt on lt.account_id= aocdcd.disposition_account_id