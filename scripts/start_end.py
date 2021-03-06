# This script contains the function for slicing the filtered 
# maf file according to a window size. 

def start_end(alignment, target_seqname, window_size):
	"""
	This function returns a list containing the start
	and end coordinates of a sliced multiple sequence 
	alignment from a generator object given a target
	species and chromosome in the form of species.chromosome.
	The slicing is done in base of the user-specified window 
	size. It also returns the number of sequences per window. 
	"""
	# Create empty list of start coordinates
	start = []
	# Create empty list of sizes
	size = []
	# For each alignment in the file
	for ali in alignment:
		# For each record in the alignment
		for record in ali:
			# Find the reference sequence
			if record.name == target_seqname:
				# Record the start position
				start.append(record.annotations['start'])
				# Record the size
				size.append(record.annotations['size'])
	# Create empty list of coordinates
	coord_lst = []
	# Save first start coordinate
	st = start[0]
	# Save first size
	sz = size[0]
	j = 0
	# For each index
	for i in range(1, len(start)):
		# If the index is not the last one
		if i < (len(start)-1):
			# If the size is smaller than the window size
			if sz+size[i] < window_size:
				# Update the accumulated size
				sz += size[i]
			# If the size is larger than the window size
			else:
				# Append start and end coordinates
				coord_lst.append((st, start[i]+size[i]-1, i-j))
				# Update the accumulated size and start position
				st = start[i+1]
				sz = size[i]
		else:
			coord_lst.append((st, start[i]+size[i]-1, i-j))
	return(coord_lst)






















