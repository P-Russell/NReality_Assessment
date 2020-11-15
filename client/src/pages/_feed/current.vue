<template>
  <div>Current</div>
</template>

<script>
export default {
  async mounted() {
    console.log(this.$api)
    const feed = await this.$api.fetchFeed(this.$route.params.feed, false)
    console.log(feed)
  },
}
</script>

<style></style>
