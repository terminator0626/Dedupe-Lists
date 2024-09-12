def deduplicate_lists(lst1, lst2, reverse=False):
    combined_list = lst1 + lst2
    unique_list = list(set(combined_list))
    return sorted(unique_list, reverse=reverse)
