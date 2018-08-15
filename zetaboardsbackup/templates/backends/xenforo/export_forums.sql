INSERT INTO `xf_node` (`node_id`, `title`, `description`, `node_name`, `node_type_id`, `parent_node_id`, `display_order`, `display_in_list`, `lft`, `rgt`, `depth`, `style_id`, `effective_style_id`, `breadcrumb_data`, `navigation_id`, `effective_navigation_id`) VALUES 

{% for forum in forums %}
({{ forum.zeta_id }}, '{{ forum.title }} ', 'Description goes here.', NULL, {% if forum.parent %}'Forum'{% else %}'Category'{% endif %}, {% if forum.parent %}{{ forum.parent_id }}{% else %}0{% endif %},1,1,2,3,1,0,0,NULL,'',''){% if not forloop.last %},{% else %};{% endif %}
{% endfor %}


INSERT INTO `xf_forum` (`node_id`, `discussion_count`, `message_count`, `last_post_id`, `last_post_date`, `last_post_user_id`, `last_post_username`, `last_thread_title`, `last_thread_prefix_id`, `moderate_threads`, `moderate_replies`, `allow_posting`, `allow_poll`, `count_messages`, `find_new`, `field_cache`, `prefix_cache`, `prompt_cache`, `default_prefix_id`, `default_sort_order`, `default_sort_direction`, `list_date_limit_days`, `require_prefix`, `allowed_watch_notifications`, `min_tags`) VALUES

{% for forum in forums %}
({{ forum.zeta_id }}, 0, 0, 0, 0, 0, '', '', 0, 0, 0, 1, 1, 1, 1, '', '', '', 0, 'last_post_date', 'desc', 0, 0, 'all', 0){% if not forloop.last %},{% else %};{% endif %}
{% endfor %}

