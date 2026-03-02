SIG: GC Project Management (EU)
Date: 2025-12-08
Duration: 34 minutes
Zoom Recording URL: https://zoom.us/rec/share/3Y97a8aVgBwspvivODBE4fuBeEunDbOr8q4FxtJxuRvyplZtAKhnDjSC6K2ap-ui.-QSoPrDQyF9wnBS6
============================================================

## Zoom Recording Transcript

**Juraci Paixão Kröhling** 02:26 Hi, Morgan.
**Severin Neumann** 02:46 Lieutenant Morgan.
Sorry. Sorry.
Hello, hello.
**Pellared** 04:32 Hello, can you hear me?
**Juraci Paixão Kröhling** 04:33 Yeah.
**Severin Neumann** 04:34 Loud and clear How's everybody doing? How was your weekend?
**Juraci Paixão Kröhling** 04:41 Yeah. It was.
**Pellared** 04:48 shorts?
**Juraci Paixão Kröhling** 04:50 Oh, yeah, I was a little bit sick the whole week. We had an offsite in Lisbon, and I was sick almost the whole week.
But, I'm better now, so…
**Severin Neumann** 05:02 That's good to hear.
Yeah.
Yeah, I'm worried that I get sick sooner than later, so…
**Juraci Paixão Kröhling** 05:09 Yeah.
**Pellared** 05:10 My daughter has ear infection since last week, but now it's getting better.
**Juraci Paixão Kröhling** 05:17 Oh my.
Damn.
**Severin Neumann** 05:21 Yeah, let's hope for the last two weeks, and then there's, like, a break, and hopefully there's, like, at least a little bit of time, too.
**Pellared** 05:28 That is now… I'm happy that she's sick, not now, not during the Christmas.
Yeah. Chapter 15.
**Severin Neumann** 05:34 Totally.
Yeah.
Yeah, my son already was, like, a week ago, like, hey, I'm done, I'm done with school.
No, I don't really feel that. Anyways, let's do some triage, right? Can I… I can share my screen if you like.
You can see that.
**Juraci Paixão Kröhling** 05:58 I can see it, yeah.
**Severin Neumann** 06:00 Yeah.
Okay, there's something about, like, adding a workflow…
To ensure change logs are added…
Okay, I don't think… We need to do a lot for triage here, right?
I would just say it's accepted.
accepted ready is probably enough, right? Because it's… it's more like a…
Infrastructure change, so it does not really need… Any additional attention?
Metric filter status…
**Pellared** 06:55 Accepted.
**Severin Neumann** 07:03 So it's more like a question? Is this even like… but anyways, let's…
**Pellared** 07:08 It's like a follow-up to update the compliance metrics.
**Severin Neumann** 07:12 Yeah, yeah.
I just mark it as accepted, so…
Wouldn't seem to understand this thing.
Declarative config support for distribution-specific config…
So this is, first of all, something that the… config.
Oh, is it stability? Because, I mean, they're stable already, right?
**Pellared** 07:45 It's not stable yet.
**Severin Neumann** 07:46 Okay. Or maybe, I'm not sure.
**Pellared** 07:49 At least it was not a week ago, but maybe it's…
**Severin Neumann** 07:56 Then I turn it into a sick issue, right?
**Pellared** 08:01 I think he's the label.
**Severin Neumann** 08:04 conflict?
I like those that are just easy, right?
Add support in SDKs in support of spec changes…
Huh.
**Pellared** 08:37 I'm not sure if you shouldn't be here.
I think it will just create issues in the specific… in the repositories.
**Severin Neumann** 08:45 I mean, at some end, it's like the tracking issue, I think it's just a sick issue. I mean, I get your point, probably it's not…
**Pellared** 08:53 Yep.
**Severin Neumann** 08:54 something, but I would just label it as a sick issue and leave it to the same config.
**Pellared** 08:59 Yeah, because there's IC, there is this CACD, I see. It's already assigned.
**Severin Neumann** 09:03 I see D… do they have a label?
**Pellared** 09:06 There's a lot of the project.
**Severin Neumann** 09:08 Which is assigned to… Yeah, it's a project, it's a SIG issue, so done.
Duplicate Jaeger propagator.
I mean, it's probably accepted, but I still think that's something the… TC should decide, right?
Andrew, do we have, like, a practice for deprecation? Like, I mean…
**Juraci Paixão Kröhling** 09:42 We just did it for Zipkin, right? And I think this one here makes a lot of sense as well, because it is, the… the Uber
Trace context headers, so… I would…
I would be in favor of the Bricketing Eager.
Yeah, there you go. Well, yeah, I mean, it's similar, but it's… yeah, it's similar, but not the same.
**Severin Neumann** 10:07 But this never… this never had an issue, right? Or is there an issue?
**Pellared** 10:12 The Jaeger exporter is already DP created, it's only about the Jaeger propagator right now, this issue.
**Severin Neumann** 10:18 Yeah, I just wanted to look for some,
Some examples where we… where we went, like, through a deprecation.
Process, and someone said, okay, let's deprecate that.
Yeah, drop support for Janka Drift.
And then… blah blah blah blah blah…
**Pellared** 10:41 an export.
**Severin Neumann** 10:42 I wonder if this is something, nevertheless, the TC should just look into, or if we just, like, yeah, it sounds, like, good, and just accept it? I don't know.
**Juraci Paixão Kröhling** 11:00 So this definitely needs TC input, yeah.
**Pellared** 11:04 I asked Yuri here, just to double check.
But if even the Jaeger says, team that is deprecated.
then I, in my opinion, we could deprecate it as well.
But, yeah, we can double-check with the technical community.
**Juraci Paixão Kröhling** 11:24 So is…
**Severin Neumann** 11:24 And by default, I'll lock.
**Juraci Paixão Kröhling** 11:27 It's not, right? And… The only one by the 4 is trace context.
**Pellared** 11:33 That's correct.
**Juraci Paixão Kröhling** 11:37 Yeah, I don't know how I feel about it. I mean, I wouldn't… I think…
legacy software doesn't just disappear. I don't know if I would be comfortable in removing the propagator, which is important for the interoperability, from the SDKs. Like, it's there, it's code that I can.
**Severin Neumann** 11:55 But I think that the question is also what deprecation means, right? I mean, does deprecation mean we remove it, or does it mean, like, for languages that have not implemented it until today, they shouldn't, right?
**Juraci Paixão Kröhling** 12:08 once, man.
**Severin Neumann** 12:09 maybe… yeah.
**Juraci Paixão Kröhling** 12:10 Yeah, can you open this link here from yogurtracing.io?
No, I think that's…
**Pellared** 12:16 It was documented in Zeekin Exporter.
I think in Zip Exporter DPR, the strategy was exactly like that, that we were deprecating, by saying that if there's a major release that has this support, then it should be kept, or something like this.
**Juraci Paixão Kröhling** 12:35 Yeah, so it's not very clear, even from the Jaeger page, what deprecated means. Like, the wire format is supported, but it's deprecated.
Like, what is deprecated? I mean, what does it mean?
I think we… if they have a definition, we could… we could just piggyback on that and say, you know, we follow the same semantics of what deprecation… deprecated means.
**Severin Neumann** 13:02 Yeah, but I said, I think at the end it's something that the TC needs to tackle and say, like, hey, this is how we do it, right? So…
**Juraci Paixão Kröhling** 13:07 I agree.
**Severin Neumann** 13:08 Bill.
Okay.
Blame for… One note off.
Okay.
It's to follow up, automation working.
Work issues for follow-up.
It's broken.
Or, like… I don't know.
A while?
**Pellared** 13:51 Okay.
**Severin Neumann** 13:52 That explains a lot.
like… It stopped working… Oi!
in August.
**Pellared** 14:05 August.
**Severin Neumann** 14:11 What has changed? Oh, you know what has changed? I think that's, like, a permission issue, I guess. So, like, the whole…
heighten 3L11 was not found on your system.
So, I think that's the problem.
Let me create an issue… Issue… blank issue… Triage, follow-up.
Workflow is broken.
Since August… Workflow to mark.
Issues… Thank you. Hello.
Up period. Triage is broken.
So let's mid-August.
Seems true.
be really intent.
I'm gonna change in the GitHub.
Runner, since the error indicates that item 3.11 Yeah, I love pool.
My profile… Runs on Ubuntu latest, yeah.
No.
I suspect it changed something in…
I give it a triage accepted, right? So, anyways…
**Pellared** 16:39 Do you want to have wasn't? Do you want to have wanted? So maybe someone will grab…
**Severin Neumann** 16:45 sponsors.
Maybe it's a simple change, I can't even look into that, but…
Put it into the TCGC channel anyways.
Okay.
Do we want also to look into the community repo for a little bit?
Or do you want to jump?
**Pellared** 17:35 Let me go inside, that's tricky.
**Juraci Paixão Kröhling** 17:37 Yep.
**Severin Neumann** 17:39 Let's quickly look into… to pull requests…
Another one is missing the project proposal label.
Check.
This is one of the issues in PRs where I would find it extremely valuable if we could signal to maintainers that it would be worthwhile for them to take a look.
See, I don't know, if we…
Yeah, but it's a different… but anyways, I just wanted to call this out.
I don't think there's anything that needs…
Triage right now, but from the issues…
Great, adjust… Generate C-Spell…
Is this infra? Let's say so, right?
Yeah, it's something I just need to do. I just… Can't do that.
What's… what's the area of licenses, then?
legal, or…
I don't know.
I mean, we still have this one open, right, with the campaigning.
**Juraci Paixão Kröhling** 20:28 Yeah. It's old.
I don't know what to take of it.
I think the only consensus is, people should not be appearing on social media, on official channels, if there are candidates around the time of the election.
**Severin Neumann** 20:43 I mean, this is something we should bring back to the GC agenda, and let's vote on it, and make a decision based on, like, the…
I mean, we have a little bit of a feedback, right? I mean…
we have at least Damien, and then we have, like, Amen, Mark.
And, yeah, there's a few votes on that, so yeah, maybe we can put it back on the…
**Juraci Paixão Kröhling** 21:09 And the agenda.
Yeah.
**Severin Neumann** 21:21 Do we already have something here?
Oh, should we just, like, since not enough people were at the meeting last week, should we just use the agenda from last week?
Yeah, that makes sense, probably.
Change that to…
Okay.
Any… any other community issues you'd like to…
Take a quick look into anything you think that's worthwhile to spend a few minutes on, or…
We just call it a day.
**Pellared** 22:45 What about this defined priority ownership of Go OpenTelements UIO?
**Severin Neumann** 22:54 It was updated.
**Pellared** 22:55 days ago, I was looking at some other issue related to this, this week.
Today.
**Severin Neumann** 23:03 I have a self-assigned advisor.
**Pellared** 23:05 see what…
**Severin Neumann** 23:07 I never… Intended to assign it.
I cannot even remember signing that.
**Pellared** 23:15 self-assigned four days ago, what's wrong with you?
Ms. Cleep?
**Severin Neumann** 23:27 Yeah, I can not remember even, like, opening up this issue on 4 days ago.
So, my… if my memory serves me correctly…
ownership of Natley Farm? First of all, I unassigned, because that makes no sense. So my understanding was that…
There was, like, a… wasn't there, like, a prototype being worked onto… To migrate down.
But it stalled also for a while, so…
So I think the idea was to have, like, a… Instead of having, like, this…
GCP machine that's doing, like, this whole very basic redirects for… for the Go installer, just to put it on a… on a Netlify instance.
But I think that's something that, like, the Ghostig needs to decide on, right? It's not something we can really…
**Pellared** 24:46 I think…
The thing is that I'm not sure if we have… the goalie has access.
to the Netlify, if something goes wrong.
Regarding certificates or whatever.
**Severin Neumann** 25:06 I mean, ideally…
**Pellared** 25:07 about… I'm not sure if it's about permissions, if there was no clarity, if we know… I think that technically we can go with it, but if we do not have permissions to, you know, manage it, it doesn't make sense. I think that was…
**Severin Neumann** 25:23 Yeah, I mean, that can be changed, right?
**Pellared** 25:26 of the Ghostik meeting.
**Severin Neumann** 25:28 I mean, that's something we can… we can work on, right? I mean, we can…
we… I think we should be able to have… people permissions on… Specific…
**Pellared** 25:45 So, is it the same Netflix… is it the same Netlify,
as for OpenTremetry I.O, because I think this, I think it should not be the same, or I think…
The idea was that it would be not the same people, so that one will not harm, you know, the other.
**Severin Neumann** 26:05 No, yeah, we can, like, under… under Netlify, We can have…
multiple projects. That's not a problem, right? We already tried this out with,
for example, you also have changelog.opentelemetry.io, not sure what turned out to be, like, the result of that project, but I can create go.opentelemetry.io even as a…
as a… as an intermediate project, and… and… and you… like, if you follow up with me on that, like, I can…
I can see that we can give the right people the right access on that.
**Pellared** 26:48 I think it makes sense… yeah, I think it was the only blocker from the GoSeq, and I think it's needed not only for the GoSeq, it's also needed for the collector, because the same, it's basically used for any Go-related, you know, resources.
**Severin Neumann** 27:06 Yeah, yeah, but, but…
**Pellared** 27:07 So, for automatic goal, yeah.
**Severin Neumann** 27:09 There's a weekend…
**Pellared** 27:10 maintainers of this Go-related distributor.
**Severin Neumann** 27:14 We can add additional people to that.
what I don't know, like, so the whole SSL stuff, that's managed by Netlify then, right? Then that's not something you need or should be worried about.
The only thing that I think once went wrong.
is that we set some specific DNS entries Deadly to… dead loud to…
Netlify giving up, like, someone said, like, hey, we are now managing… like, without intent, we told Netlify by setting that, DNS entry, like, we are now managing SSL on our own, right? I think there was something around that, that by setting the CAA,
entry… there's something in their docs that you should really only do that if you… if you manage your SSL certifications yourself, which we don't want to, right? Is my understanding. Like, I'm totally fine with Netlify taking care of that, and…
And, and rolling that and everything.
But yeah, I mean, just let me know, or let anybody else from… from… so it could be… me…
Patrice… I think Trask also has access
To… to that extent, so… so we could help you with that.
**Pellared** 28:33 the… I think the best…
I think the best what you could do, if you have time, of course, if you just try to follow up with Damien on it. But I think that what you told is, you know, the way to go. I think we just, like, you know, engagement on it and transparency.
And I think it just got stale, because, you know, just, you know, there was a proposal to Netlify, but some things were not answered. Maybe… I think there were… these questions were asked probably even during the Ghostic meeting, when reviewing Dames PR, I think…
Damien also had… I'm not sure if he also had described the concerns, so just, you know, it's just about, you know, following up. I don't think it will take a lot of time, but just… Yeah. I think just having it open…
It's not good for us.
**Severin Neumann** 29:20 Yeah, I mean, I can… let me… I can…
I can tack him here.
No, I cannot, because, like, my browser's just… Stalling on everything.
yeah.
**Pellared** 29:36 And Damien is also online right now, probably you could even sync with him on Slack.
**Severin Neumann** 29:41 Yeah.
I mean, if you like, you can also shoot him and myself a message, and then we can…
We can… we can work on that together, so… yeah.
Just shoot him a message, and then we can take it from there.
**Pellared** 30:00 Okay.
Oh, fuck, yeah.
**Severin Neumann** 30:02 Yep.
**Pellared** 30:05 We'll go.
**Severin Neumann** 30:05 Anything else?
**Pellared** 30:08 That's all for my sake.
**Severin Neumann** 30:13 Okay, Dan, talk to you.
Soon? I guess. Bye-bye.
**Juraci Paixão Kröhling** 30:19 Alright, see ya, folks, bye.
**Pellared** 30:20 Recover your resty.
Bye.
**Juraci Paixão Kröhling** 30:22 Thank you. Thanks.
