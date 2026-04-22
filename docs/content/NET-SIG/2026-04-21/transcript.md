SIG: .NET SIG
Date: 2026-04-21
Duration: 12 minutes
============================================================

## Zoom Recording Transcript

**Martin Costello** 00:09 Hey, Matt.
Hey, Matt.
**Matthew Hensley / Grafana Labs** 00:36 Hello.
**Martin Costello** 00:41 Are you feeling bad?
**Matthew Hensley / Grafana Labs** 00:41 Perhaps.
Kinda, just had migraine problems, and now internet problems, so…
**Martin Costello** 00:52 Yeah, my internet's been weird the last week or so as well.
**Matthew Hensley / Grafana Labs** 01:10 I was expecting there to be a lot of people.
**Martin Costello** 01:14 How come?
**Matthew Hensley / Grafana Labs** 01:16 Just with all the… Potential releases, and… Such.
**Martin Costello** 01:22 Alright.
I know Alan isn't coming.
I haven't heard anything from Raj.
Have you got anything you want to discuss?
**Matthew Hensley / Grafana Labs** 02:05 Not today.
**Martin Costello** 02:11 Might be a short meeting if it's just me and you.
**Matthew Hensley / Grafana Labs** 02:16 Yeah, if there's any PRs or anything… like, another set of eyes on, I'm happy to take a look.
**Martin Costello** 02:29 Is that you who's opened the dock?
**Matthew Hensley / Grafana Labs** 02:31 No.
**Martin Costello** 02:32 I'm guessing it's Judeus. A dudious.
**Julius Koval** 02:35 How's it going?
**Martin Costello** 02:37 Good, thanks, how are you?
**Julius Koval** 02:40 Yeah, I'm good, thanks.
**Martin Costello** 02:46 I was just saying to Matt, it might be a short meeting today if there aren't many people.
Do you have anything that you want to discuss, Julius?
**Julius Koval** 03:30 Not really, I was just… Wondering, have you taken a look at my PR?
**Martin Costello** 03:38 Which one?
**Julius Koval** 03:39 Key-value list.
**Martin Costello** 03:41 I haven't, no.
**Julius Koval** 03:43 Yeah, all good.
Nothing else for me.
**Martin Costello** 03:52 Just give me a second to… open up GitHub, and then… Okay, I haven't heard anything from Raj, so I guess it's just me.
Ed… Everyone see the screen?
**Julius Koval** 04:41 Yeah, I see it.
**Martin Costello** 04:45 Cool. So, the only thing… Oh, yeah.
But two quick things I had on the agenda. One was… We shipped a new release today, so pretty much, if you use a hotel package that comes from either our repos, there's new versions. A bunch of, issues have been fixed.
That's it, really. It's just sort of like a release announcement.
There's quite a large PR review backlog, but it's almost exclusively caused by me.
and I can't progress my own PRs without approvals.
And… I think I need them from the maintainers as well, and I'm the only one of us who's here right now, so… There's not much that can be done there, but if anyone wants to… review any of the open PRs and give any feedback.
That would be welcome, even if they don't give the magic green tick.
Tons of new issues since last week.
So, I opened an issue… I can't remember if we discussed this last week or not. I opened an issue to track. We had a request to help move along the Prometheus stuff to stable, so there's an issue here tracking, adding some new settings. Someone's picked that up, already, so there's a PR open for that. There'll probably be more stuff we need to do to stabilize the Prometheus stuff, but I haven't gone through the spec to find all the gaps yet, but there is an issue linked on this issue… yeah, these two. I think there's a table in them that has all the outstanding work that needs to be done, so if anyone fancies digging through that and seeing what there is… the money done doing PRs, that'd be welcome.
Pull requests… Let's see what I mean, they're almost all me.
I think this… So, Julius says you're here, was there anything on this other than, please, can people have a look at it?
**Julius Koval** 07:13 Well, yeah, I, added a list for the… You know, nesting depths or whatever.
And so that's something I wanted to discuss with others, because, like I mentioned, it's probably not in the spec.
**Martin Costello** 07:32 Oh, I see you've put something in. What I… I'll try and take a look at this this week. I've been busy the last week.
If you could spin up an issue in the semantic conventions… repository.
Sure. Ask about… The limits here, because either there is one and you haven't found it, which means it might be buried away and needs making more prominent, or we don't have one at all and we probably should.
So, we can press ahead with your PR as it is if you've put in, like, a guard to make you do something sane.
And then we can just hold on a definitive answer from that, and then react to that when… once we have one.
**Julius Koval** 08:19 Yeah, I set the limit to 3, just arbitrarily for now.
**Martin Costello** 08:24 Okay, that's fine. But yeah, then once we've got some steer from the semantic conventions people.
then we can react to that in your PR.
But yeah, I'll try and look at this for you this week.
**Julius Koval** 08:38 Okay, cool.
**Martin Costello** 08:42 And then for Contrope, what have we got that's new? Someone's, I think… Metrics to surface fabric stuff?
There's a few issues that Steve Gordon from Elastic has opened for the op-amp work.
And I think that's it. New stuff, and then pull requests… There's a few to, like, fix up some flaky tests that we've started acquiring.
And… there's some other miscellaneous bug fixes we've got.
If anyone's got pre-time… I would like to do any PRs. There's, there's an issue here tracking… adding the schema URLs to all the… tracer metrics instrumentation. This should be a full list of all the components. I've been trying to chip through them slowly, one by one, but If anyone would like to pick up one that hasn't already got PR against it.
That'd be welcome.
Otherwise, I think that's… All there is at the moment.
Is there anything else either of you would like to discuss?
**Julius Koval** 10:14 Not from me.
**Matthew Hensley / Grafana Labs** 10:16 Nope, I'm good.
**Martin Costello** 10:18 Cool. Well, in that case, that's a… that's a lightning round, 10-minute meeting.
Alright, thanks for attending, and I'll see you next time.
**Julius Koval** 10:26 Thanks, man.
