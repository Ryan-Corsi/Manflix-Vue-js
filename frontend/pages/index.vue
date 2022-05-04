<template>
  
  <div
    class="main 
    flex align-items-center
    justify-content-center flex-column w-screen h-screen
    "
  >
    <div class="logo">
      <img src="../static/logo.png" >
    </div>
    <div
      class="p-4 
      login-container 
      flex align-items-center 
      justify-content-center flex-column w-screen h-screen 
      md:w-3 md:h-auto"
      style="background-color: rgba(0,0,0,.75); color:white;"
    >
      <h2>Login</h2>
      <p class="p-input-icon-left w-full" style="margin-top: 20px;">
        <i class="pi pi-user" />
        <InputText class="w-full" type="text" placeholder="Usuário" style="height: 40px; background-color: #333; border: none;"
        v-model="user.username"/>
      </p>
      <p class="p-input-icon-left w-full" style="margin-top: 20px;">
        <i class="pi pi-lock"/>
        <InputText class="w-full" type="password" placeholder="Senha" style="height: 40px; background-color: #333; border: none;"
        v-model="user.password"/>
      </p>
  
      <p>
        <Button label="Entrar" 
        class="p-button-raised p-button-secondary"
        style="background-color:red; border-color:red; margin-top: 20px; height: 40px" 
        v-on:click="sendLogin()"/>
      </p>
      <br/>
      <p class="texto">Novo por aqui... <a class="link-reg" href="/register" >Cadastre-se</a></p>
    </div>
  </div>
</template>

<script>

export default {
  name: "IndexPage",
  data(){
    return{
      user:{
        username: '',
        password: ''
      }
    }
  },
  methods:{
    sendLogin: function(){
      if(this.user.username && this.user.password)
      {
        this.$auth.loginWith(
          "local", {data: this.user}
        ).then(()=>{
          alert("Usuário logado!");
        })
      }
      else{
        alert("Preencha todos os campos!");
      }
    }
  }
};
</script>

<style lang="scss" scoped>
  @import "@/layouts/scss/reset.scss";

  .main{
    background-repeat: no-repeat; 
    background-size: cover; 
    background-image: url('https://images8.alphacoders.com/107/thumb-1920-1073623.jpg'); 
    width: 100%; 
    display: row; 
    justify-content: center; 
    align-items: center;
  }

  .logo{
    height:150px;
    width:150px;
    align-self: start;
    padding-left: 20px;
    position: absolute;
    top: 0;
    margin-top: 40px;
  }

  .w-full{
    color:white;
  }
  
  .link-reg{
    color: white;
  }
  
  a{
    text-decoration: none;
  }

  a:hover {
    text-decoration: underline;
  }
  
  .texto{
    color: grey;
  }

  i{
    width:10px;
  }
</style>
