<template>
  <div class="container">
    <div class="row justify-content-center">
      <div class="col-12 text-center py-3">
        <h3 class="text-muted">{{ $route.params.feed }}'s Read Later List</h3>
      </div>
      <FeedList
        v-if="entries && entries.length"
        :entries="entries"
        class="col col-12 col-lg-8"
      />
      <Alert v-else-if="error" type="danger">{{ error }}</Alert>
      <Spinner v-else-if="loading" :size="3" class="mt-4" />

      <Alert v-else-if="entries && entries.length === 0" type="info"
        >No entries for {{ $route.params.feed }} found</Alert
      >
    </div>
  </div>
</template>

<script>
import FeedList from '~/components/feed_list'
import Spinner from '~/components/spinner'
import Alert from '~/components/alert'

export default {
  name: 'ReadLater',
  layout: 'results',
  components: { FeedList, Spinner, Alert },
  data() {
    return {
      entries: null,
      error: null,
      loading: false,
    }
  },
  async mounted() {
    try {
      this.loading = true
      this.entries = await this.$api.fetchFeed(this.$route.params.feed, true)
    } catch (e) {
      this.error = 'User Not Found'
    } finally {
      this.loading = false
    }
  },
}
</script>
