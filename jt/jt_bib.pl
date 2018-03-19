#!/usr/local/bin/perl
#
#Converts Jonathan's publication list into bibtex entries
#written 2002, Jayesh Ramanlal Version 1.1
#
#To use the script you use:
#1.copy and paste the orignal html file to another file
#ie http://www.tampa.phys.ucl.ac.uk/jonny/pubs.html
#This is need to remove the html tags, 
#nb may need to add a few empty line to the end of the file
#
#2.run the script
#  perl jt_bib.pl file [start number]
#where
#The file is a non-html list on the publications
#The entries are numbers so the conversion can start a a particular postion
#if omited then the convesion starts at the begining.
#
#OUTPUT, outputs is to standard output

use strict;

my ( $author, $title, $journal, $year, $volume, $pages);
my ($paper_number, $paper_start) = 0;

#open input file
open MY_INPUT, $ARGV[0]
  or die "Error opening input file ($!)";

if($ARGV[1]) {
   $paper_start = $ARGV[1];
}

while (<MY_INPUT>) {
    chomp;

    if (/^([\d]{1,3})/) { #paper number
      $paper_number = $1;}

    if($paper_number >= $paper_start){

    if (/([\d]{1,3}\.).*\>(.*Tennyson.*)\\\\/) { #authors
      $author = $author . $2;
      $author =~ s/(,\s*)$//; #get rid of comma at the end
      $author =~ s/(, )/ AND /g; #repace commas with AND
      $author =~ s/\ and / AND /g; #change case on rememaining 'and'
    }


    elsif (/(\\>)(.*)\\\\\*/) { #title
      if ($2 =~ /^ ([A-Z].*),/) {
	$title = "{" . $1 . "}";
      }
    }

    elsif (/\\it ([A-Z][\w. ]+)/) { #journal
      $journal = $1;
}

    if (/\(((19|20)\d\d)\)/) { #year
      $year = $1;
}

    if (/\\bf (\d{1,})/) { #volume number
      $volume = $1;
    }

    if (/(\d{1,}-\d{1,})/) { #page numbers
      $pages = $1;
       }

#finds a blank line as the end of entry then outputs matched data
    if (/^$/) {
#      print "END OF ENTRY \n";

      print "\@Article{jt$paper_number ,\n";
      print "author = {$author},\n";
      print "title = {$title},\n"; 
      print "journal = {$journal},\n";
      print "year  = {$year},\n" if ($year); 
      print "volume  = {$volume},\n" if ($volume); 
      print "pages = {$pages}\n" if ($pages); 
      print "OPTfile_num = {$paper_number}\n" if ($paper_number);
      print "}\n\n";

      #zero variables
      ($author, $title, $journal, $year, $volume, $pages, $paper_number) =0;
    }
  }

  }

#close file
close MY_INPUT;
