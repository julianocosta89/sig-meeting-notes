SIG: OpenTelemetry C/C++ SIG
Date: 2025-12-15
Duration: 9 minutes
Zoom Recording URL: https://zoom.us/rec/share/VTJXI-WTEyJL2fiNxQa8N3snSp6O7XFDt61jXIAXKsGhfL0uNdcEkvdBoHS154s.K6a7lowOfbNvUYuO
============================================================

## Zoom Recording Transcript

**Marc Alff [MySQL]** 03:05 How are you, son.
**Ehsan** 03:08 Hi, Mark.
**Marc Alff [MySQL]** 03:17 Do you know if, Lalit or Tom or, Duke are joining today?
**Ehsan** 03:24 No idea.
**Marc Alff [MySQL]** 03:26 Okay.
just to let you know, Duke has a PR, but, approved and merged to…
improve ceiling tidy. So, in CI, we have a much better CI now that reports a lot of things.
So, there will be probably a lot of, cleanup to do in this area.
**Ehsan** 04:03 Yeah, nice.
**Marc Alff [MySQL]** 04:07 And… Just to show you how it works.
If I can't find it… Okay.
In the summary, he's generating a report.
With all the details, by file.
With the details by file, and so things like that, and also by type of errors.
So, this report is actually quite nice to look at.
And then you have… Of course, each, each channel.
**Ehsan** 04:55 How is the report generated?
**Marc Alff [MySQL]** 04:58 It's… I didn't look at the detail, but it's a huge Python script, which is running in CI.
Scrape the logs from ceiling tidy.
And make a report out of it.
So, just so you know, some nice features, and…
No, of course, we have some cleanup to do.
**Ehsan** 05:29 Yeah, it sounds like a lot.
**Marc Alff [MySQL]** 05:32 Yep.
I'm assuming there will be nobody around for Christmas, so the next two meetings are canceled.
Oh.
I'm not sure if you saw that earlier or not.
**Ehsan** 05:59 Yeah, I was just checking.
**Marc Alff [MySQL]** 06:02 Okay.
Okay, looks… I'm not sure if the others are coming. Do you have anything to discuss in particular?
Not really, okay.
I looked… I looked a bit… I mean, there is only two new issues and nothing much going on.
And we had a lot of PRs, but most of those were…
the Renovate CI that just upgrade,
versions to use in CI with, tags, so those have been…
Merge to trunk… to… to remain vitality.
Nothing new beside that.
**Ehsan** 07:03 Okay, thanks.
**Marc Alff [MySQL]** 07:19 Are you going to be around for… in December or not?
**Ehsan** 07:23 Yeah, this, I'm, I'm, I'm gold this year.
**Marc Alff [MySQL]** 07:30 Okay.
**Ehsan** 07:32 It'll be…
**Marc Alff [MySQL]** 07:34 Okay. I will probably do some, small cleanup,
Either in the Yaval area, or in the Silentadi area, with small piers once in a while.
So, if you're enrolled, if you could take a look and approve them. I mean, review them when they come back.
**Ehsan** 07:54 Sure, sure.
**Marc Alff [MySQL]** 07:56 True.
**Ehsan** 07:56 In case I didn't react, it would be nice if you write me on the stack.
**Marc Alff [MySQL]** 08:01 Cool.
I mean, if you're… if you're not available, I mean, it's… it's not urgent either, it's,
Just trying to keep myself busy a bit.
**Ehsan** 08:15 Yeah, I'll be available.
**Marc Alff [MySQL]** 08:18 Okay.
**Ehsan** 08:22 Hopefully everything went a little bit quiet.
**Marc Alff [MySQL]** 08:24 Yes.
No.
Yeah, being on call in the end of the Euro, it's… Another friend time.
**Ehsan** 08:35 I mean…
**Marc Alff [MySQL]** 08:35 Usually, because…
**Ehsan** 08:37 one sleep.
**Marc Alff [MySQL]** 08:41 Yeah, I'm lucky because I'm not on call, so I'm on vacation, actually, for real.
**Ehsan** 08:47 Yeah, that's cool.
**Marc Alff [MySQL]** 08:54 Okay, well, if you don't have anything special, I think we can make a very close short call.
**Ehsan** 09:01 Alright.
**Marc Alff [MySQL]** 09:02 Okay, thanks for… yeah, thanks, Issan, for stopping by.
**Ehsan** 09:07 That's fair enough.
**Marc Alff [MySQL]** 09:08 Have a good, vacation then.
**Ehsan** 09:11 Yeah, thanks, you too.
**Marc Alff [MySQL]** 09:12 Yep.
