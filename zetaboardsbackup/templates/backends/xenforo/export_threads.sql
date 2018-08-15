INSERT INTO `xf_thread` (`thread_id`, `node_id`, `title`, `reply_count`, `view_count`, `user_id`, `username`, `post_date`, `sticky`, `discussion_state`, `discussion_open`, `discussion_type`, `first_post_id`, `first_post_likes`, `last_post_date`, `last_post_id`, `last_post_user_id`, `last_post_username`, `prefix_id`, `tags`, `custom_fields`) VALUES

{% for thread in threads %}
({{ thread.zeta_id }}, {{ thread.forum.zeta_id }}, '{{ thread.title }}', {{ thread.replies }}, {{ thread.views }}, {{ thread.user.zeta_id }}, '{{ thread.username }}', {{ thread.date_posted|date:"U" }}, 0, 'visible', 1, '', 1, 0, 0, 0, 0, '', 0, 'a:0:{}', 'a:0:{}'){% if not forloop.last %},{% else %};{% endif %}
{% endfor %}

