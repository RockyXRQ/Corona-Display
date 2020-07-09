<template>
  <v-container class="mx-auto">
    <v-card class="mx-auto">
      <v-card-title>
        国内
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
        expanded.sync="expanded"
        :headers="areaHeaders"
        :items="items"
        item-key="provinceName"
        :items-per-page="5"
        multi-sort
        :search="search"
        show-expand
        :single-expand="singleExpand"
      >
        <template v-slot:expanded-item="{ item }">
          <td :colspan="areaHeaders.length">
            <v-data-table
              class="mx-auto mt-4 mb-4 elevation-0"
              dense
              :headers="cityHeaders"
              hide-default-footer
              :items="item.cities"
              item-key="cityName"
              multi-sort
            ></v-data-table>
          </td>
        </template>
      </v-data-table>
    </v-card>
  </v-container>
</template>

<script>
export default {
  name: "AreaDataTable",
  data: () => {
    return {
      expanded: [],
      singleExpand: true,
      search: "",
      areaHeaders: [
        {
          text: "名称",
          align: "center",
          sortable: false,
          value: "provinceName"
        },
        { text: "潜在感染数", align: "center", value: "suspectedCount" },
        { text: "当前确诊", align: "center", value: "currentConfirmedCount" },
        { text: "累计确诊", align: "center", value: "confirmedCount" },
        { text: "累计死亡", align: "center", value: "deadCount" },
        { text: "累计治愈", align: "center", value: "curedCount" },
        { text: "", align: "center", value: "data-table-expand" }
      ],
      cityHeaders: [
        {
          text: "城市名称",
          align: "center",
          sortable: false,
          value: "cityName"
        },
        { text: "潜在感染数", value: "suspectedCount" },
        { text: "当前确诊", value: "currentConfirmedCount" },
        { text: "累计确诊", value: "confirmedCount" },
        { text: "累计死亡", value: "deadCount" },
        { text: "累计治愈", value: "curedCount" }
      ],
      items: []
    };
  },

  watch: {},

  methods: {
    DataUpdate() {
      this.$axios
        .get("/data/area_data.json")
        .then(response => (this.items = response.data));
    }
  },
  created: function() {
    this.DataUpdate();
    setInterval(this.DataUpdate, 180000);
  }
};
</script>