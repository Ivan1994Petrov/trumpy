<template>
  <div class="">
    <div class="row">
      <div class="col-md-12 text-center">
        <column-chart :data="columnData.order_data_by_hours" title="Tweets by time of the day" label="Tweets"
        xtitle="Hours" ytitle="Tweets"></column-chart>
      </div>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src

import axios from "axios"

export default {
  name: 'home',
  components: {

  },
  data() {
      return {
          columnData : [],
      }
  },
  methods: {
      getData(){
        axios.get("http://127.0.0.1:8000/tweets-by-time-of-day/")
        .then(res =>(this.columnData = res.data))
        .catch(err => console.log(err));
      }
  },
  created() {
      this.getData()
  },
}
</script>
