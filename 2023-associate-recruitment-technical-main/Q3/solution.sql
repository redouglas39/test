SELECT o.owner_id, o.owner_name, COUNT(DISTINCT c.category_id) AS different_category_count
FROM owner o
  JOIN article a ON a.owner_id = o.owner_id
  JOIN category_article_mapping cam ON cam.article_id = a.article_id
  JOIN category c ON c.category_id = cam.category_id
GROUP BY o.owner_id, o.owner_name
ORDER BY different_category_count desc;
