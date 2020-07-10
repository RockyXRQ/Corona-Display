<template>
  <v-container class="mx-auto">
    <v-card class="mx-auto">
      <v-card-title>
        全球
        <v-spacer></v-spacer>
        <v-text-field
          v-model="search"
          append-icon="mdi-magnify"
          color="#38D993"
          dense
          label="Search"
          hide-details
          single-line
        ></v-text-field>
      </v-card-title>
      <v-data-table
        class="elevation-1"
        color="#38D993"
        :headers="headers"
        :items="items"
        item-key="provinceName"
        :items-per-page="5"
        multi-sort
        :search="search"
      >
        <template v-slot:item.incrVo.currentConfirmedIncr="{item}">
          <v-chip
            :color="getConfirmedColor(item.incrVo.currentConfirmedIncr)"
            dark
          >{{item.incrVo.currentConfirmedIncr}}</v-chip>
        </template>

        <template v-slot:item.incrVo.confirmedIncr="{item}">
          <v-chip
            :color="getConfirmedColor(item.incrVo.confirmedIncr)"
            dark
          >{{item.incrVo.confirmedIncr}}</v-chip>
        </template>

        <template v-slot:item.incrVo.curedIncr="{item}">
          <v-chip :color="getCuredColor(item.incrVo.curedIncr)" dark>{{item.incrVo.curedIncr}}</v-chip>
        </template>

        <template v-slot:item.incrVo.deadIncr="{item}">
          <v-chip :color="getDeadColor(item.incrVo.deadIncr)" dark>{{item.incrVo.deadIncr}}</v-chip>
        </template>
      </v-data-table>
    </v-card>
  </v-container>
</template>

<script>
export default {
  name: "CountryDataTable",
  data: () => {
    return {
      search: "",
      headers: [
        {
          text: "名称",
          align: "center",
          sortable: false,
          value: "provinceName"
        },
        { text: "累计确诊", align: "center", value: "confirmedCount" },
        {
          text: "累计确诊变化",
          align: "center",
          value: "incrVo.confirmedIncr"
        },
        { text: "累计死亡", align: "center", value: "deadCount" },
        { text: "累计死亡变化", align: "center", value: "incrVo.deadIncr" },
        { text: "累计治愈变化", align: "center", value: "incrVo.curedIncr" },
        { text: "病死率(%)", align: "center", value: "deadRate" }
      ],
      items: []
    };
  },

  methods: {
    DataUpdate() {
      this.$axios.get("/data/country_data.json").then(response => {
        this.items = response.data;
      });
    },
    getConfirmedColor(increase) {
      if (increase > 1000) return "red";
      else if (increase > 200) return "orange";
      else if (increase > 0) return "yellow";
      else return "green";
    },
    getCuredColor(increase) {
      if (increase > 100) return "green";
      else if (increase > 50) return "yellow";
      else return "red";
    },

    getDeadColor(increase) {
      if (increase > 10) return "red";
      else if (increase > 0) return "yellow";
      else return "green";
    }
  },
  created: function() {
    this.DataUpdate();
  },

  mounted: function() {
    this.timer = setInterval(this.DataUpdate, 180000); //定时间隔，
  },

  destroyed: function() {
    clearInterval(this.timer);
    this.timer = null;
  }
};
</script>