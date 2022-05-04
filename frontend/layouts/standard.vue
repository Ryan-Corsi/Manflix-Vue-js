<template>
  <div>
    <header class="flex flex-row align-items-center justify-content-between">
      <!-- colocar this.$router quando for chamar no script -->
      <!-- <a v-on:click="$router.push('/home')">Home</a> -->
      <!-- <a v-on:click="$router.push('/about')">About</a> -->
      <button
        class="pi pi-bars btnHamburger"
        v-on:click="showSidebar = showSidebar ? false : true"
      />      
      <div class="logo">
        <img src="../static/logo.png" >
      </div>

      <button class="avatarUser" v-on:click="showDetails = showDetails ? false : true">
        <Avatar
          :image="$store.state.BASE_URL + $store.state.usuario.foto"
          size="xlarge"
          shape="circle"
          v-if="$store.state.usuario.foto"  
        />
        <Avatar
          image="sem_foto.jpg"
          size="xlarge"
          shape="circle"                
          v-else
       />


      </button>

    
     
    </header>

    <Dialog 
      :visible.sync="showDetails"
      class="customDetails"    
    >
      <template #header>
	    	<h3>Informações</h3>
	    </template>
       <h3>Usuário: {{$store.state.usuario.nome}}</h3>
       <br/>
        <div
        v-for="(myButton, index) in buttonLogout"
        :key="index"
        class="btnLogout"
      >
        <button class="btnLogout"
          v-on:click="
            () => {
              if (myButton.path === 'logout') $auth.logout();
              else $router.push(myButton.path);
            }
          "
        >
          
          <span>Sair</span>
        </button>
      </div>
       
    </Dialog>

    <Sidebar
      :visible.sync="showSidebar"
      :dismissable="true"
      :baseZIndex="1000"
      :showCloseIcon="false"
      class="customSidebar"
    >
      <div
        v-for="(myButton, index) in buttonsSidebar"
        :key="index"
        class="btnContainer"
      >
        <button
          v-on:click="
            () => {
              if (myButton.path === 'logout') $auth.logout();
              else $router.push(myButton.path);
            }
          "
        >
          <i :class="myButton.icon" />
          <span>{{ myButton.name }}</span>
        </button>
      </div>
    </Sidebar>


  
    <Nuxt/>
    <footer></footer>
  </div>
</template>

<script>
export default {
  data() {
    return {
      dados:  null,
      showSidebar: false,
      showDetails: false,
      buttonLogout: [
        {
          name: "Logout",
          path: "logout",
        }
      ],
      buttonsSidebar: [
        {
          icon: "pi pi-home",
          name: "Home",
          path: "/home",
        },
        {
          icon: "pi pi-info-circle",
          name: "About",
          path: "/about",
        },
        {
          icon: "pi pi-question-circle",
          name: "Help",
          path: "/help",
        },
        {
          icon: "pi pi-search",
          name: "Search",
          path: "/search",
        },
        {
          icon: "pi pi-sign-out",
          name: "Logout",
          path: "logout",
        },
      ],
    };
  },
  methods: {},
  created() {    
    console.log(this.$auth);
    this.$axios
      .get( this.$store.state.BASE_URL + "/usuarios?user=" + this.$auth.$state.user.id)
      .then((response) => {
        console.log("deu certo");
        console.log(response.data[0]);
        
        //aciona a action!
        this.$store.dispatch("SET_USER", response.data[0]);
        this.dados = response.data[0];
        console.log(this.dados);

      })
      .catch((error) => {
        console.log("deu merda");
        console.log(error);
      });
  },
};
</script>

<style lang="scss" scoped>
$height-header: 80px;
header {

  .logo{
    width: 180px;
  }

  width: 100vw;
  height: $height-header;
  background-color: var(--background-header);
  color: white;
  
  .avatarUser {
    width: auto;
    cursor: pointer;
    background: none;
    border: none;
    margin-right: 30px;
    cursor: pointer;
    transition: 0.5s;
    &:hover {
      transform: scale(1.1);
      transition: 0.5s;
    }
    
  }
  .btnHamburger {
    background-color: var(--background-header);
    color: white;
    border: none;
    width: 30px;
    height: 70%;
    margin-left: 10px;
    cursor: pointer;
    &:hover {
      background-color: var(--background-header-hover);
    }
  }

  
}

.customDetails {
  margin-right: 500px;
  position: fixed;
  padding-left: 10px;
  z-index: 1000;
  width: 300px;
  height: 300px;
  background-color: none;
  overflow: 'visible'

  
}

.btnLogout {
  color: white;
  background-color: red;
  cursor: pointer;
  border-color: red;
  height: 40px;
}

.customSidebar {
  width: 10vw;
  height: calc(100vh - $height-header);
  display: absolute;
  top: $height-header;
  left: 0;
  background-color: var(--background-sidebar);
  .btnContainer {
    width: 100%;
    height: 60px;
    // background-color: yellow;
    margin-top: 20px;
    button {
      background-color: var(--background-sidebar);
      border: 0;
      color: rgb(235, 219, 219);
      font-size: 25px;
      cursor: pointer;
      i {
        font-size: 25px;
      }
      &:hover {
        background-color: var(--background-sidebar-hover);
      }
    }
  }
}


</style>