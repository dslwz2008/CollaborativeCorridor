package com.vge.collaboration;

import com.smartfoxserver.v2.entities.User;
import com.smartfoxserver.v2.entities.data.ISFSObject;
import com.smartfoxserver.v2.entities.data.SFSObject;
import com.smartfoxserver.v2.extensions.BaseClientRequestHandler;

import java.util.List;

/**
 * Created by VGE on 2017/9/12.
 */
public class EnterMainHandler extends BaseClientRequestHandler {
    @Override
    public void handleClientRequest(User user, ISFSObject isfsObject) {
        CorridorExtension evcExt = (CorridorExtension) getParentExtension();
        evcExt.enteredUsers.add(user);
//        List<User> users = evcExt.getParentRoom().getUserList();
        //如果全部进来的话，就可以开始了
        if(evcExt.enteredUsers.size() == evcExt.userNum) {
            send("AllEntered", SFSObject.newInstance(), evcExt.enteredUsers);
        }
    }
}
