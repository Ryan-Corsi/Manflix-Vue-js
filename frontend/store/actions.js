export default {
    SET_USER(context, payload){
        console.log("vuex:" + payload);
        context.commit("USER", payload);
    }
}