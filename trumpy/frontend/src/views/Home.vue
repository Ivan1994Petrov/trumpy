<template>
  <div class="home">
    <h1>Some Graphs of Donald's Posts with Django and Vue js</h1>
    
    <TweetsVsRetweets msg="Tweets vs Retweets Pie Chart"/>
    <div class=divider></div>
    <TweetsByTimeOfDay msg="Tweets By Time Of Day Chart"/>
    <div class=divider></div>
    <MostCommonWords msg="Most Common Words Chart"/>
    
  </div>
</template>

<script>
// @ is an alias to /src
import TweetsVsRetweets from "@/components/TweetsVsRetweets.vue"
import TweetsByTimeOfDay from "@/components/TweetsByTimeOfDay.vue"
import MostCommonWords from "@/components/MostCommonWords.vue"

export default {
  name: 'home',
  components: {
    TweetsVsRetweets,
    TweetsByTimeOfDay,
    MostCommonWords,
  },
}
</script>

<style scoped>
.divider{
    height:25px;
}
</style>
