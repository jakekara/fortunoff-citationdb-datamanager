#!/usr/bin/env python

"""
    Command line tool to create and update CitaionDB data.

    See README for usage
"""

from CitationData import CitationData
from Downloader import Downloader
import argparse
import sys
import json


def convert(in_dir, out_dir, get_func, ext):
    try:
        cd = CitationData(in_dir, ext=ext)
        print("Loaded data from '%s'" % in_dir)
        get_func(cd)(out_dir)
        print("Saved data to '%s'" % out_dir)
    except Exception as e:
        print("Something went wrong when trying to convert files")
        print(e)


def json2csv(in_dir, out_dir):
    """
    Convert JSON files in in_dir to CSV files in out_dir.
    Will create destination folders if not existent.
    """
    convert(in_dir, out_dir, lambda x: x.to_csvs, "json")


def csv2json(in_dir, out_dir):
    """
    Convert CSV files in in_dir to JSON files in out_dir.
    Will create destination folders if not existent.
    """
    convert(in_dir, out_dir, lambda x: x.to_jsons, "csv")


def download_from_urls(url_file, out_dir):
    print("Downloading data from URLS in %s to %s" % (url_file, out_dir))
    dl = Downloader(json.loads(open(url_file).read()))
    dl.save_files(out_dir)


def main():
    """
    Parse arguments. See README for complete usage.
    Does not handle errors, so the program will crash if something goes wrong.
    Typically, if the source folder doesn't exist or contain all of the expected files,
    or the destination cannot be created and written to, then the program will crash.

    Input folder expected to contain:
        author.[json|csv]
        footnote.[json|csv]
        publication.[json|csv]
        resource.[json|csv]

    Where the resource is the same for all files in the folder.

    Use the json2csv subcommand if you have JSON and want CSV.

    Use the csv2json subcommand if you have CSV and want JSON.

    """
    parser = argparse.ArgumentParser(
        description='Format CSV data for CitationDB')
    parser.set_defaults(which="invalid")

    subparsers = parser.add_subparsers(help='Subcommands')

    csv2json_parser = subparsers.add_parser(
        'csv2json', help='Convert a folder of CSV files to JSON files')
    csv2json_parser.set_defaults(which="csv2json")

    json2csv_parser = subparsers.add_parser(
        'json2csv', help='Convert a folder of JSON files to CSV files')
    json2csv_parser.set_defaults(which="json2csv")

    for p in [csv2json_parser, json2csv_parser]:
        p.add_argument("--input-dir", "-i",
                       help="input directory to find files", required=True)
        p.add_argument("--output-dir", "-o",
                       help="output directory to save files",
                       required=True)

    downloader_parser = subparsers.add_parser(
        'download-csvs',
        help='Download files from a URLs JSON file'
    )
    downloader_parser.add_argument(
        "--urls-file", "-u",
        help="A JSON file containing a dictionary of URLs for each table.",
        required=True
    )
    downloader_parser.add_argument(
        "--output-dir", "-o",
        help="output directory to save files",
        required=True
    )
    downloader_parser.set_defaults(which="downloader")

    args = parser.parse_args(sys.argv[1:])

    if (args.which == "csv2json"):
        csv2json(args.input_dir, args.output_dir)
    elif (args.which == "json2csv"):
        json2csv(args.input_dir, args.output_dir)
    elif(args.which == "downloader"):
        download_from_urls(args.urls_file, args.output_dir)
    else:
        parser.print_help()
        exit(-1)


if __name__ == "__main__":
    main()
