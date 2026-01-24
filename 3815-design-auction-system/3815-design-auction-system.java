import java.util.*;

class AuctionSystem {

    // Represents a single bid
    private static class Bid {
        int userId;
        int itemId;
        int amount;

        Bid(int userId, int itemId, int amount) {
            this.userId = userId;
            this.itemId = itemId;
            this.amount = amount;
        }
    }

    // itemId -> ordered bids
    private Map<Integer, TreeSet<Bid>> itemBids;

    // "userId#itemId" -> Bid (for fast lookup)
    private Map<String, Bid> bidLookup;

    public AuctionSystem() {
        itemBids = new HashMap<>();
        bidLookup = new HashMap<>();
    }

    // Comparator: by amount, then userId
    private TreeSet<Bid> getBidSet(int itemId) {
        return itemBids.computeIfAbsent(itemId, k ->
            new TreeSet<>((a, b) -> {
                if (a.amount != b.amount) {
                    return a.amount - b.amount;
                }
                return a.userId - b.userId;
            })
        );
    }

    private String key(int userId, int itemId) {
        return userId + "#" + itemId;
    }

    public void addBid(int userId, int itemId, int bidAmount) {
    String k = key(userId, itemId);

    // If bid already exists, remove it first (REPLACEMENT behavior)
    if (bidLookup.containsKey(k)) {
        Bid oldBid = bidLookup.get(k);
        TreeSet<Bid> set = itemBids.get(itemId);
        set.remove(oldBid);
    }

    Bid newBid = new Bid(userId, itemId, bidAmount);
    TreeSet<Bid> set = getBidSet(itemId);
    set.add(newBid);
    bidLookup.put(k, newBid);
}


    public void updateBid(int userId, int itemId, int newAmount) {
        String k = key(userId, itemId);
        Bid bid = bidLookup.get(k);

        TreeSet<Bid> set = itemBids.get(itemId);
        set.remove(bid);           // remove old
        bid.amount = newAmount;    // update
        set.add(bid);              // reinsert
    }

    public void removeBid(int userId, int itemId) {
        String k = key(userId, itemId);
        Bid bid = bidLookup.remove(k);

        TreeSet<Bid> set = itemBids.get(itemId);
        set.remove(bid);

        if (set.isEmpty()) {
            itemBids.remove(itemId);
        }
    }

    public int getHighestBidder(int itemId) {
        TreeSet<Bid> set = itemBids.get(itemId);
        if (set == null || set.isEmpty()) {
            return -1;
        }
        return set.last().userId;
    }
}
