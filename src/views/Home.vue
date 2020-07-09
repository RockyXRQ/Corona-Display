<template>
  <div class="home">
    <CountryDataTable></CountryDataTable>
    <AreaDataTable></AreaDataTable>
  </div>
</template>

<script>
// @ is an alias to /src
import CountryDataTable from "@/components/CountryDataTable.vue";
import AreaDataTable from "@/components/AreaDataTable.vue";

export default {
  name: "Home",
  components: {
    CountryDataTable,
    AreaDataTable
  }
};
</script>
