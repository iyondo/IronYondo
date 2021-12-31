create database publication;
use publication;

#Challenge 1
SELECT a.au_id, a.au_lname, a.au_fname, ti.title, p.pub_name
  FROM authors a
  INNER JOIN titleauthor ta ON a.au_id=ta.au_id
  INNER JOIN titles ti ON ti.title_id=ta.title_id
  INNER JOIN publishers p ON p.pub_id=ti.pub_id;
  


#Challenge 2
SELECT a.au_id, a.au_lname, a.au_fname, ti.title, p.pub_name, s.qty
  FROM authors a
  INNER JOIN titleauthor ta ON a.au_id=ta.au_id
  INNER JOIN titles ti ON ti.title_id=ta.title_id
  INNER JOIN publishers p ON p.pub_id=ti.pub_id
  FROM
  INNER JOIN sales s ON s.title_id=