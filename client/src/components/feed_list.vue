<template>
  <div>
    <div v-for="entry in entries" :key="entry.id" class="card m-3">
      <FeedItem :entry="entry" />
    </div>
  </div>
</template>

<script>
import FeedItem from './feed_item'
export default {
  name: 'FeedList',
  components: { FeedItem },
  props: {
    entries: {
      type: Array,
      required: true,
    },
  },
}
</script>
