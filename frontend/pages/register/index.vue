<template>
  <div
    class="
      main
      flex
      align-items-center
      justify-content-center
      flex-column
      w-screen
      h-screen
    "
  >
    <div class="logo">
      <img src="../../static/logo.png" />
    </div>
    <div
      class="
        p-4
        login-container
        flex
        align-items-center
        justify-content-center
        flex-column
        w-screen
        h-screen
        md:w-4 md:h-auto
      "
      style="background-color: rgba(0, 0, 0, 0.75); color: white"
    >
      <div class="mid-topo" style="display: inline-flex">
        <h2>Registre-se</h2>
        <a href="/"
          ><i
            class="pi pi-arrow-left"
            style="
              font-size: 1.6rem;
              color: white;
              padding-left: 260px;
              padding-top: 5px;
            "
        /></a>
      </div>
      <p class="p-input-icon-left h-auto w-full" style="margin-top: 20px">
        <i class="pi pi-user" />
        <InputText
          class="w-full"
          type="text"
          placeholder="Nome completo"
          v-model="user.fullname"
          style="height: 40px; background-color: #333; border: none"
        />
      </p>
      <!-- <p class="p-input-icon-left h-auto w-full" style="margin-top: 20px;">
        <i class="pi pi-user" />
        <InputText
          class="w-full"
          type="text"
          placeholder="Usuário"
          v-model="user.username"
          style="height: 40px; background-color: #333; border: none;"
        />
      </p> -->
      <p class="p-input-icon-left h-auto w-full" style="margin-top: 20px">
        <i class="pi pi-envelope" />
        <InputText
          class="w-full"
          type="text"
          placeholder="Email"
          v-model="user.email"
          style="height: 40px; background-color: #333; border: none"
        />
      </p>
      <p class="p-input-icon-left h-auto w-full" style="margin-top: 20px">
        <i class="pi pi-phone" />
        <InputText
          class="w-full"
          type="text"
          placeholder="Telefone"
          v-model="user.phone"
          style="height: 40px; background-color: #333; border: none"
        />
      </p>
      <p class="p-input-icon-left h-auto w-full" style="margin-top: 20px">
        <i class="pi pi-id-card" />
        <InputText
          class="w-full"
          type="text"
          placeholder="CPF"
          v-model="user.cpf"
          style="height: 40px; background-color: #333; border: none"
        />
      </p>
      <p class="p-input-icon-left h-auto w-full" style="margin-top: 20px">
        <i class="pi pi-moon" />
        <InputText
          class="w-full"
          type="date"
          placeholder="Data de Nascimento"
          v-model="user.dtNascimento"
          style="
            height: 40px;
            background-color: #333;
            border: none;
            cursor: pointer;
            
          "
        />
      </p>
      <p class="p-input-icon-left h-auto w-full" style="margin-top: 20px">
        <i class="pi pi-lock" />
        <InputText
          class="w-full"
          type="password"
          placeholder="Senha"
          v-model="user.password"
          style="height: 40px; background-color: #333; border: none"
        />
      </p>
      <p class="p-input-icon-left h-auto w-full" style="margin-top: 20px">
        <i class="pi pi-lock" />
        <InputText
          class="w-full"
          type="password"
          placeholder="Confirme Senha"
          v-model="user.passConfirm"
          style="height: 40px; background-color: #333; border: none"
        />
      </p>

      <p>
        <Button
          label="Registrar"
          class="p-button-raised p-button-secondary"
          v-on:click="sendRegister()"
          style="
            background-color: red;
            border-color: red;
            margin-top: 20px;
            height: 40px;
          "
        />
      </p>
    </div>
  </div>
</template>

<script>
export default {
  name: "IndexPage",
  data() {
    return {
      user: {
        fullname: "",
        dtNascimento: "",
        username: "",
        password: "",
        passConfirm: "",
        email: "",
        phone: "",
        cpf: "",
        idUser: 0,
      },
    };
  },
  methods: {
    sendRegister: function () {
      console.log(this.user);
      if (this.user.password === this.user.passConfirm) {
        this.registerUser();
      }
    },
    registerUser: function () {

      const body = {
        username: this.user.email,
        password: this.user.password,
        email: this.user.email,
      };

      console.log("body")
      console.log(body)


      this.$axios
        .post(this.$store.state.BASE_URL + "/api/v1/users/", body)
        .then((response) => {
          console.log("cadastro do user ok");
          console.log(response);
          this.user.idUser = response.data.id;
          this.registerUsuarios();
        })
        .catch((error) => {
          console.log("cadastro do user ERRADO!");
          console.log(error);
          this.user = null;
        });
    },
    registerUsuarios: async function () {
      const body = [
        {

          nome: this.user.fullname,
          idUser: this.user.idUser,
          email: this.user.email,
          fone: this.user.phone,
          ativo: false,
          foto: null,
          cpf: this.user.cpf,
          dtNascimento: this.user.dtNascimento,
        },
      ];

      this.$axios
        .post(this.$store.state.BASE_URL + "/usuarios/", body)
        .then((response) => {
          console.log("cadastro do USUARIO ok");
          console.log(response);
          alert("CRIADO COM SUCESSO");
        })
        .catch((error) => {
          console.log("cadastro do USUARIO ERRADO!");
          console.log(error);
        });
    },
  },
};
</script>

<style lang="scss" scoped>
@import "@/layouts/scss/reset.scss";
.main {
  background-repeat: no-repeat;
  background-size: cover;
  background-image: url("https://images8.alphacoders.com/107/thumb-1920-1073623.jpg");
  width: 100%;
  display: row;
  justify-content: center;
  align-items: center;
}

.logo {
  height: 150px;
  width: 150px;
  align-self: start;
  padding-left: 20px;
  position: absolute;
  top: 0;
  margin-top: 40px;
}

.w-full {
  color: white;
}




i {
  width: 10px;
}

::-webkit-calendar-picker-indicator {
  filter: invert(1);
  padding-right: 15px;
}

::placeholder { /* Chrome, Firefox, Opera, Safari 10.1+ */
  color: grey;
  opacity: 1; /* Firefox */
}

:-ms-input-placeholder { /* Internet Explorer 10-11 */
  color: grey;
}

::-ms-input-placeholder { /* Microsoft Edge */
  color: grey;
}
</style>


