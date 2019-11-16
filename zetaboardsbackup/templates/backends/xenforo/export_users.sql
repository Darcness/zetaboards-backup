INSERT INTO `xf_user` (`user_id`, `username`, `email`, `custom_title`, `language_id`, `style_id`, `timezone`, `visible`, `activity_visible`, `user_group_id`, `secondary_group_ids`, `display_style_group_id`, `permission_combination_id`, `message_count`, `conversations_unread`, `register_date`, `last_activity`, `trophy_points`, `alerts_unread`, `avatar_date`, `avatar_width`, `avatar_height`, `avatar_highdpi`, `gravatar`, `user_state`, `is_moderator`, `is_admin`, `is_banned`, `like_count`, `warning_points`, `is_staff`, `secret_key`) VALUES

{% for user in users %}
({{ user.zeta_id }}, '{{ user.username }}', 'example-{{ user.username|slugify }}@example.com', '', 1, 0, 'America/Los_Angeles', 1, 1, 2, '', 2, 3, {{ user.post_count }}, 0, {{ user.date_joined|date:"U"}}, 0, 0, 0, 0, 0, 0, 0, '', 'valid', 0, 0, 0, 0, 0, 0, 'BorkBorkBork'){% if not forloop.last %},{% else %};{% endif %}
{% endfor %}

INSERT INTO `xf_user_profile` (`user_id`, `dob_day`, `dob_month`, `dob_year`, `signature`, `website`, `location`, `following`, `ignored`, `avatar_crop_x`, `avatar_crop_y`, `about`, `custom_fields`, `connected_accounts`, `password_date`) VALUES

{% for user in users %}
({{ user.zeta_id }}, {{ user.date_birthday|date:"j"|default:0 }}, {{ user.date_birthday|date:"n"|default:0 }}, {{ user.date_birthday|date:"Y"|default:0 }}, '{{ user.signature }}', '', '', '', 'a:0:{}', 0, 0, '', 'a:3:{s:5:"skype";s:0:"";s:8:"facebook";s:0:"";s:7:"twitter";s:0:"";}', 'a:0:{}', 1){% if not forloop.last %},{% else %};{% endif %}
{% endfor %}

INSERT INTO `xf_user_privacy` (`user_id`, `allow_view_profile`, `allow_post_profile`, `allow_send_personal_conversation`, `allow_view_identities`, `allow_receive_news_feed`) VALUES

{% for user in users %}
({{ user.zeta_id }}, 'everyone', 'everyone', 'everyone', 'everyone', 'everyone'){% if not forloop.last %},{% else %};{% endif %}
{% endfor %}
