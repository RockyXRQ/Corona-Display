<template>
  <v-app>
    <v-app-bar app color="white" dense>
      <v-spacer></v-spacer>
      <div class="d-flex align-center">
        <v-img
          alt="Vuetify Logo"
          class="shrink mr-2"
          contain
          src="./assets/logo.png"
          transition="scale-transition"
          width="55"
        />
        <v-btn text dense>
          <span>Corona-Display</span>
        </v-btn>
      </div>
      <v-spacer></v-spacer>
    </v-app-bar>

    <v-main app>
      <router-view></router-view>
    </v-main>
  </v-app>
</template>

<script>
export default {
  name: "App",

  components: {},

  data: () => ({
    //
  })
};
</script>
