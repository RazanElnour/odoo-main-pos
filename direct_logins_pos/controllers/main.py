# -*- coding: utf-8 -*-
from odoo.http import request
from odoo.addons.web.controllers.main import Home as HomeOld

class Home(HomeOld):
    def _login_redirect(self, uid, redirect=None):
        if redirect:
            return redirect
        else:
            if request.session.uid:  # fully logged
                user = request.env['res.users'].browse(uid)
                if user.pos_config_id and user.direct_login:
                    pos_session = request.env['pos.session'].sudo().search([('config_id', '=', user.pos_config_id.id),('rescue', '=', False),('state', '=', 'opened')])
                    #  Open POS session only if it is already opened by the same user or if it is closed
                    if len(pos_session)>0:
                        redirect = user.pos_config_id.open_ui()['url']
                    else:
                        user.pos_config_id.open_session_cb()
                        pos_session = request.env['pos.session'].sudo().search(
                                [('config_id', '=', user.pos_config_id.id), ('rescue', '=', False),
                                 ('state', '=', 'opening_control')])
                        pos_session.action_pos_session_open()
                        redirect ='/pos/web?config_id='+str(user.pos_config_id.id)
                return redirect or '/web'
