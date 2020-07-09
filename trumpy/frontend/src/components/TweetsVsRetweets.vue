<template>
  <div class="">
    <div class="row">
      <div class="col-md-12 text-center">
        <pie-chart :data="pieData.pie" title="Tweets vs retweets"></pie-chart>
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
          pieData : [],
      }
  },
  methods: {
      getData(){
        axios.get("http://127.0.0.1:8000/tweets-vs-retweets/")
        .then(res =>(this.pieData = res.data))
        .catch(err => console.log(err));
      }
  },
  created() {
      this.getData()
  },
}
</script>
