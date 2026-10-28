# Public suffix snapshot

`public_suffix_list.dat` is the unmodified official snapshot downloaded from
[publicsuffix.org](https://publicsuffix.org/list/public_suffix_list.dat).
Its embedded version and commit identify the exact input. The upstream MPL 2.0
notice is retained in the file. See the [upstream instructions](https://publicsuffix.org/list/).

CI reads the checked-in snapshot without network access. To update it, download
the official file, review its version/diff, and run the indicator tests plus
`python bin/validate.py` and `python bin/validate_generated.py`.

The validator applies ICANN exact, wildcard, exception, and implicit `*` rules.
General-purpose shared hosting/service roots are also checked in
`bin/domain_safety.py`. Private suffixes can represent cataloged remote-access
services themselves (for example ngrok), so they are not all categorically
rejected. Add shared hosts with evidence and regression coverage.
