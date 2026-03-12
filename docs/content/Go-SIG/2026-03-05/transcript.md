SIG: Go SIG
Date: 2026-03-05
Duration: 27 minutes
============================================================

## Zoom Recording Transcript

**Tyler** 00:14 Hey, Sam.
**Sam Xie** 00:19 They live?
**Tyler** 00:20 How's it going?
**Sam Xie** 00:22 Good. How about you?
**Tyler** 00:24 Good.
Good, yeah. This, media, I'm guessing, is hanging for you as well, right?
**Sam Xie** 00:30 Alright.
**Tyler** 00:31 Yeah, I don't know what's going on here.
**Sam Xie** 00:40 Maybe they are using the same system.
Of the Canadian.
**Tyler** 00:45 Yeah, that's usually what caused it. I don't remember what the fix was, but I thought Trask, like, went through and got it all.
like, got a lot more seats or something like that? I can't remember exactly what caused…
**Sam Xie** 00:57 Perfects, but…
**Tyler** 01:00 Yeah, that's kind of weird.
Usually it was, like, a previous meeting that was the same one. Someone just didn't log out.
**Sam Xie** 01:10 Oh, they're either late delivery?
**Tyler** 01:12 Yeah.
I guess, like, the answer is maybe, like, just go into that meeting and then… take the… the… I don't know, what's the admin role or something like that, and then… Try to end it there, but…
**Sam Xie** 01:25 Any second.
**Tyler** 01:26 Yeah.
Hey, David. Hey, Robert.
**Pellared** 01:33 Oh, in mazes.
**Tyler** 01:35 Yeah.
You did?
**Pellared** 01:40 Bye.
**Tyler** 01:48 Cool. I guess we're 3 minutes in, starting a little late due to that, but I can start sharing my screen in just a second. If you haven't yet, it looks like everyone's already added their names on the attendees list. If you have agenda items you wanted to talk about, go ahead, add them there as well, and yeah, let's, Let's jump in here.
Yeah, so I… the only thing that I added is, looking at the next, milestone. This is something that Robert was kind of… I think more leading, so I wanted to just check in on this and see what your thoughts on it are, Robert.
Around, like, what we need to do before… oh.
Oh, that's why it automatically.
**Pellared** 02:32 operation.
**Tyler** 02:33 The link there.
**Pellared** 02:33 But I didn't want to change it because I didn'.
**Tyler** 02:36 No, that's true.
**Pellared** 02:36 Bye.
**Tyler** 02:37 No, I had it, like, yeah, I had it all set up, Google Auto did some things there. Alright, everyone.
We'll just… just do the old manual. Yeah.
Do it live, as they say, right?
Okay, cool. So.
**Pellared** 03:01 The first two PR… the one PR regarding empty, not critical, can be moved, it's just very small.
I just thought that we can add it, but if you don't have time to review, then whatever.
**Tyler** 03:17 It looks like we already have one review on this, so this is just looking for more reviews, and this is going to resolve the other thing, yeah.
Is Tracer provider Tracer?
Sorry, go ahead.
**Pellared** 03:26 I think David… David blocked on the specification. I think that's really still waiting on your approval on the specification, Tyler. If I'm… Nope, I think…
**David Ashpole (dashpole)** 03:36 I just approved it, yeah.
**Tyler** 03:38 It merged yesterday.
**Pellared** 03:40 Okay, so it's unblocked right now, correct?
**David Ashpole (dashpole)** 03:43 Except now we need the opposite of this PR. Or, like, we need to add…
**Tyler** 03:48 Yeah, it needs to change, it needs to not be removed, it needs to be changed, yeah.
I'm gonna just close this, because that's not… this isn't the right approach, yeah.
**Pellared** 04:01 Do we want to make a PR to enhance this documentation?
for this release, it should be a straightforward question is regarding the time for you, Tyler, because I'm not… Right, not 100% sure what… Pipes methods should be documented.
**Tyler** 04:21 All the… all the methods outside of the link…
**Pellared** 04:25 Type itself.
**Tyler** 04:26 But that's not really possible to be documented as concurrency, but .
**Pellared** 04:30 Yeah. Struck.
**Tyler** 04:32 Yeah.
But yeah, essentially just all the methods. One of the things we did talk about in the metrics one, David, was that, like, we had documented each method, because that's what the spec said, but, like, we had always talked about, like, also documenting, like, the… the top level that all the methods need to be, like, implementations of those, need to be concurrent safe, right? And so that way, it can actually show up in the docs, not in, like, the code snippet in the docs, yeah.
**Pellared** 04:57 Sir?
**David Ashpole (dashpole)** 04:59 Yeah, we can always tweak it. Do people care if I separate out PRs by signal type, or should I just… make all the updates. I think the logging one merged. Am I mistaken?
**Pellared** 05:11 This is Easter.
**David Ashpole (dashpole)** 05:12 after logging.
**Pellared** 05:13 Metrics is already merged, I think, unless there have been some changes. I think the only thing left was for tracing.
**Tyler** 05:19 Yeah, logging always is documented this way.
**David Ashpole (dashpole)** 05:22 Oh, really? Yeah. Okay, that's funny.
Our logging, or the spec?
**Tyler** 05:26 are, are…
**Pellared** 05:27 boring.
**David Ashpole (dashpole)** 05:28 Yeah. Right, right, but the spec…
**Tyler** 05:31 Oh, sorry, yeah, at the spec level, no. Logging hasn't been merged at the spec level. I don't… I don't think that's the case.
Actually, I'm not sure about the spec level, but yeah, metrics and traces at the spec level are… yeah, sorry, that was the spec.
**David Ashpole (dashpole)** 05:43 I'll just… I'll open a PR just to update traces, and if we decide to do, We just did a release, right? So I can go look at the GoDocs.
**Tyler** 05:57 Days ago.
**David Ashpole (dashpole)** 05:57 I dislike them.
And then decide to do different things for metrics.
**Tyler** 06:01 Yeah.
**Pellared** 06:02 Here, we can…
**Tyler** 06:04 See that really quick.
**Pellared** 06:14 I think, like…
**David Ashpole (dashpole)** 06:16 So if you look at, like… There. So you can see it.
And I don't think it… so basically what you're saying is it would show up in the text.
**Pellared** 06:26 above float64 counter, if I put it…
**Tyler** 06:30 It would show up right here, yeah, so if you document the thing that would, in the code, go above here, that would show up here, and this is the part that people read.
**Pellared** 06:38 I'm not sure, to be honest. If someone implemented the method, I'm not sure could highlight.
**Tyler** 06:44 You're not what?
**Pellared** 06:46 I… I think that you're reading it, I think someone is implementing the methods.
I would say that my guess is 80% of the readers are looking at the stuff, what this method is about.
**Tyler** 06:59 Okay.
**David Ashpole (dashpole)** 07:00 Just put it in both places, but…
**Tyler** 07:02 This… this doesn't… this'll show up in your editor. This will show up in any sort of, like, documentation from the editor that it puts into the interface itself. This won't.
**Pellared** 07:14 This does not…
**Tyler** 07:15 Show up.
**David Ashpole (dashpole)** 07:18 What editor?
**Pellared** 07:19 It's.
**David Ashpole (dashpole)** 07:19 editor. She's dumb.
**Pellared** 07:21 Yeah, I guess it depends on, like, what editor you're using, but, like, I mean, like, I use Vim.
**Tyler** 07:25 Love you both.
VS Code or something like that, and if you ask for, like, the docs of a particular, like, signature, like.
you can usually, like, you know, get function docs or that kind of thing, like, it won't give you the method docs of the implementation. It'll give you the interface itself docs, but that's not… that's this. It's not this.
**David Ashpole (dashpole)** 07:44 Yep.
**Tyler** 07:46 So, I…
**David Ashpole (dashpole)** 07:48 We can just put it in both.
**Tyler** 07:50 I mean, I think it's subjective, but, like, yeah, I do think that, like, that's… that's why I was saying it. Yeah, both seems… I mean, well, yeah, I don't… I don't think we should remove this, I just think that we should probably add it is what I'm… yeah, I agree, yeah.
**Pellared** 08:02 Just think about removing this one, yeah.
**Tyler** 08:06 No, that's a… that's a whole can of worms you don't want to open.
Yeah, so I think adding it here just would be… it'd be easier for developers who are trying to implement the interface to find it, is the only thing. But it's also not, like… I don't even think it's, like, top 5 things of things you need to get done in this project, so, if that's not something you want to work on, I understand it.
It's not…
**David Ashpole (dashpole)** 08:32 It's helpful.
**Tyler** 08:33 Then, alright, I… I also recognize prioritization is completely personal, so, yeah, cool.
Right, so then, yeah, then outside of that, the other milestone, rebuild SemConf and verify… oh, yeah, I opened this PR.
Looks like Robert commented on it.
I don't follow… why we would need to update the CI workflow?
**Pellared** 09:11 Right now, the CI is using… There is a cache for the tools.
NT.
Do… go check out.
then it loses the timestamps, and make files are based on the timestamps, basically. It recognizes what should be rebuilt based off the timestamps.
So… If we add to the… dependencies that go some, and we do not update the timestamps, it will always need to be rebuilt, on the CI.
all the tools, so our…
**Tyler** 09:51 Why… why isn't that currently the case?
**Pellared** 09:54 Because we have only GoMode, and here, if you look above, you have this file name equals go mode.
And it has the go mode for the tools, as you can see.
So, yeah, that's why it's working currently on CI.
**Tyler** 10:12 Yeah, alright.
I can update to… update the CI, then.
**Pellared** 10:16 Yes, sure, yeah.
**Tyler** 10:17 Yeah.
**Pellared** 10:19 And the second one, because it's about SamConfKit. So, basically, these two tools will need to be rebuilt every time, because… oh, maybe I'm wrong?
Very… yeah.
Verify files, yeah, because then we'll need to basically timestamp for all these files, I don't think it's worth, but these are just only two tools which are quick to build, so I do not care about rebuilding those two files. I'm also not sure if those two… yeah, this was also cached, but yeah, I don't care about those two.
**Tyler** 10:55 So, see, I never call SimComp Kit.
That's only done.
Locally.
**Pellared** 10:59 The Verify REME.
**Tyler** 11:03 The Verify README might be called, because I think that that might be a part of, like, the default, linting, so that might be… need to be fixed.
But I can take a look at that.
**Pellared** 11:12 breaker. I think it's cool.
**Tyler** 11:14 No, it is also pretty small, but yeah.
Yeah, this is more the one that, like, I was interested in, because every time I…
**Pellared** 11:22 Yes, you can have a buck because of it.
**Tyler** 11:24 Could… Yeah, it's like every time that I do this, where I change code there, and then, like, it's like 5 times I try rerunning it, and it doesn't apply because I haven't rebuilt it.
**Pellared** 11:33 I just want to say that, why do you even want to undergo some to the dependencies.
Why do we even need this?
**Tyler** 11:45 Why do you need it?
I don't know, I mean, I guess… I guess if GoMod changes is really… GoSum's gonna change. I guess the only thing is, is, like, if you cleaned up GoSum…
**Pellared** 11:57 those two should change always together. Yeah, so it's just, like, definitely in-depth, I assume.
**Tyler** 12:04 Hmm.
Yeah, I don't know, I just saw that it was there, and it was… seemed like… I don't know why you wouldn't have both of them there, but.
**Pellared** 12:12 Yeah, you can. Not a problem. I was just thinking that.
**Tyler** 12:14 Yeah, no, I mean, okay, that makes sense. We don't… we don't particularly need it.
Yeah, I can remove, I can remove that.
**Pellared** 12:23 Okay.
**Tyler** 12:24 Yeah, it's more about this. This is the one that I cared about.
More than any of them. So, yeah. And then I just did the verified readmees, because it was also a tool we built, so… I imagine it's gonna be the same thing.
Yeah, okay, I'll… I'll update after… after the call.
**Pellared** 12:42 Awesome.
**Tyler** 12:43 Any other… issues or pull requests that we need to include in this milestone? I know, Robert, you're trying to get another release out soon, right, if I'm not mistaken?
**Pellared** 12:53 is I want to start releasing to tomorrow, basically. So, whatever… whatever will be, I don't know, PRs created by David, by you, Tyler, I will just merge them tomorrow morning. I do not think any, you know, substantial things… Okay. That needs to be addressed, and I will just resolve it even 3 or 24 hours, merge 3 or 2 to 24 hours, and start the release process.
**Tyler** 13:16 Okay. Does it make sense for all of you?
Yeah, what are we trying to get out in this next release? Sorry.
For Mrs.
**Pellared** 13:25 Templant, mostly, because…
**Tyler** 13:27 Okay, yeah.
**Pellared** 13:27 Correct.
**David Ashpole (dashpole)** 13:29 Okay.
**Tyler** 13:30 I was trying to figure out why we're, like…
**David Ashpole (dashpole)** 13:32 I thought we just did a release.
We usually do a microwave dish.
Two months.
**Damien Mathieu** 13:40 Even every quarter, probably, these past few months.
**Tyler** 13:45 Yeah.
But yeah, I think you're right, Robert. SEMCOMP is a great reason to get this out. Does that make sense?
And SEPCOM fixes, actually. There's a lot of…
**Pellared** 13:55 Yeah. Improvement.
**Tyler** 13:57 Yeah, we just fixed. Okay, and then, have you also taken a look at the contrib, milestones?
Robert, or are they as… not as, there's only one thing I saw here, this deprecate the read bytes stuff, here.
**Pellared** 14:13 The rest, I think, is already merged.
And with this one, I think the problem… I'm not sure.
**Tyler** 14:28 conflicts… Looks like it's… so it looks like it's more just waiting on cleanup, right?
**Pellared** 14:36 Damien, do you want to… do you have time to clean it up?
**Damien Mathieu** 14:41 Not today.
**Pellared** 14:43 Tomorrow morning.
**Damien Mathieu** 14:44 I can do that tomorrow morning, yes.
**Pellared** 14:47 Okay.
**Damien Mathieu** 14:48 Yeah, I can… Picks the conflict and push to that branch.
**Pellared** 14:53 Okay, so, let's try doing it tomorrow morning.
This is a simple PR.
**Tyler** 14:58 Yeah, otherwise, I think if, Damien, you can't get to it, we can bump this out of the next release. I don't think it's critical, but…
**Damien Mathieu** 15:04 Yeah, I think it's also… it doesn't have to be shipped, with this release, it can go with the next one.
**Pellared** 15:10 like, I want to have it shipped because it just increases the chance of stable auto HTTP. I'm not sure how much, but…
**Damien Mathieu** 15:17 Yes, on that, I agree. I'll do that tomorrow… tomorrow morning.
**Tyler** 15:23 Cool. Awesome.
Any other… Issues or things that we're missing here that people would like to get in and contribute?
Within the next 24 hours?
What's going on here? Oh, right. Now we're on a pinned version.
Wait, is this still? This is 3 days ago.
Oh…
**Pellared** 15:55 So work?
**Tyler** 15:57 Yeah, I think this might be… Is this still?
**David Ashpole (dashpole)** 16:01 Oh, no.
Isn't that?
**Damien Mathieu** 16:04 because we are using the main release, like, main branch for SimConf.
**Tyler** 16:13 Yeah, that is the case, I think, with all this, like, hashed ones, but I did see… Oh, maybe it got… Like, this… this is interesting.
**Pellared** 16:23 Strange, but maybe it's a bug in the renovate?
**Tyler** 16:27 Yeah, I do kind of remember once in a while this happens, but I can't remember, like, I thought we fixed a lot of this stuff.
I don't know how to search, actually, in the PR. Sometimes.
Yeah, I'm guessing there's just things that are… Not loading down at the bottom here.
**Pellared** 16:45 You need to scroll through the bottom has, probably.
**Tyler** 16:48 Yeah.
There we go.
Oh, this, okay, so this just merged.
**Pellared** 16:59 was just merged. Yep.
**Tyler** 17:01 Okay, so that's…
**Pellared** 17:02 proven merged.
**Tyler** 17:03 That's fine, that makes sense.
And then… yeah, it doesn't… that's actually not even as… important, right? Because this'll just get bumped in the next release.
Yeah. So, yeah, we don't even need this, okay.
Cool.
To grow this… I don't think I see anything else.
Huh.
Is this… I thought this merged in upstream, right?
**Pellared** 17:42 Nobody reviewed.
Yeah. You can adjust the milestone.
That's sealing issues, possibly.
**Tyler** 17:49 This looks like it's actually ready to merge. I don't think it needs to block, but… yeah, maybe I'll… should I add it to this milestone? I'm happy to review this after this call, but…
**Pellared** 17:58 Yes, as it increases the chance that I will merge tomorrow morning.
**Tyler** 18:02 Okay, cool.
Okay, awesome.
Come back to the agenda, I… those are the two things I wanted to go through. Sorry about the links. Any other topics y'all had?
Or things you wanted to talk about?
**Pellared** 18:24 So, there was this security vulnerability that was, like, we have.
I just want to have any response from the TC or others before we do anything.
I also do not seem as critical. When I calculated this EVV, it was, like, moderate. It requires a man in the middle.
So, I don't think it's critical that it needs to be solved in, you know, just ASAP. I will just wait until we have an agreement with other languages how we want to solve it.
Any comments?
**Tyler** 19:10 Like, I… I'm…
**Pellared** 19:12 I want to give it one week.
**Tyler** 19:15 Yeah, I think maybe that's the way to… because I wouldn't want this just to, like, be un…
**Pellared** 19:20 Nope.
**Tyler** 19:20 I want to fix that. I want to get rid of it.
And I don't think that you're gonna get a lot of movement from the TC on this.
I guess we have a TC member here. Maybe David could take a look at it? Yeah.
**David Ashpole (dashpole)** 19:34 I mean, I agree with the assessment that it seems like Not the biggest.
It feels like a… like a stack overflow in the kernel or something, where it's like, yeah, there's probably lots of them.
**Pellared** 19:48 Yeah, it will create issues for it, probably there'll be tons of it.
**David Ashpole (dashpole)** 19:52 But… I think it's worth fixing.
I don't feel like we need to wait for Java to fix theirs, too. But I do agree that, like, we should some… I don't know if we should file, like, a whole bunch of medium… vulnerabilities, or just open a spec PR to… Require it, and then… Let all the language maintainers know.
It would seem odd if we treated it as a vulnerability just for our package, and that everyone else, like.
It wasn't going for it.
**Pellared** 20:27 The thing which I would like to have an agreement on, on a spec level, or prosper level, whatever, is what is the limit, what is the size?
So, we do not make a cup if someone, you know, some vendor, for instance, make a big basin as a response, or whatever, and we'll cut it because we will say, oh, we want only, you know, 1 kilo, I don't know, 10 bytes?
Or whatever.
I just want to have a reasonable limit. That's from… From other vendors, or yeah, whatever.
**David Ashpole (dashpole)** 20:59 I feel like… Even something very high would be fine. It just has to not be able to oom your process, right?
**Pellared** 21:05 Yep.
**David Ashpole (dashpole)** 21:07 Which is…
**Pellared** 21:07 I propose 10 kilobytes, I'm not sure if it's big enough or not, maybe it should be 1 pound.
**David Ashpole (dashpole)** 21:11 The main thing people are putting in the response is that, like, partial success thing, right?
**Tyler** 21:16 Yeah.
**David Ashpole (dashpole)** 21:17 So, it's like, how big of an error message do we want to allow?
Probably, like… Do we have limits for, like, the size of a stack trace or anything?
**Pellared** 21:30 Probably.
**David Ashpole (dashpole)** 21:31 Okay.
**Tyler** 21:33 Yep.
**David Ashpole (dashpole)** 21:34 Yep, okay.
**Tyler** 21:37 I mean, I do think that, yeah, I mean, yeah, no.
I, I don't know, robert, you might just want to, like.
Yeah, I mean, I think maybe to your point, Robert, of, like, a vendor coming in and saying, like.
This is breaking my response from my endpoint.
We could always treat that as a bug, I guess?
And get feedback from them.
**Pellared** 22:04 Yes, and later fixes.
**Tyler** 22:06 Yeah, and we could always increase it.
So yeah, maybe just looking at, like, the OTLP payloads.
Taking, like, the average size of, like, the most, like.
The biggest size that can ever respond from the collector, and then, you know, order of magnitude more than that.
And I think, just start there.
**David Ashpole (dashpole)** 22:29 I've definitely seen, like, working with our own OTLP endpoint, I've definitely seen, like.
Someone just append, like, join a bunch of errors, where the error is per, like, metric point or something?
Sorry.
I'm not gonna be shocked when someone hits it, but I feel like, yeah, some reasonable limit will be fine. Yeah, there are definitely cases I've seen where people put things in the error message that probably shouldn't.
Or need to be trained.
I don't know.
**Pellared** 22:58 That's really beautiful.
10 kilobytes was 1 kilobyte.
**David Ashpole (dashpole)** 23:04 Yeah.
**Tyler** 23:09 Yeah, that makes sense.
**David Ashpole (dashpole)** 23:10 That makes sense to me, too.
I think if you can… if you have time to open a PR to the spec to put it in, I feel like that would be very useful for people, even if the number is completely wrong to start.
otherwise, I guess the other thing we can do is, like, file security vulnerabilities for everyone.
Make sure that it takes a different number.
**Pellared** 23:32 But…
**David Ashpole (dashpole)** 23:33 Yeah.
**Tyler** 23:36 Yeah, I mean, there you go. Just crowdsource it. Have everybody make their own number, and then just pick the average of them, yeah.
Oh.
**David Ashpole (dashpole)** 23:45 That noodle pole or something.
**Tyler** 23:50 Yeah, make sure you get some malicious out.
They're on that, too. Yeah, yeah, exactly, yeah.
I think it should be 2 gigs, yeah. Cool, yeah, that makes sense.
**Sam Xie** 24:05 I don't know.
**Tyler** 24:06 Cool. Any other, maybe cool things people have been working on? I know we've got KubeCon coming up as well. It sounds like… I think we might have asked how many people are going, I don't know if anybody… too many people on the call are. But, yeah, there's also the Maintainer Summit. I think people are asking to make sure we go, so if you're, I guess, coming, you should go to that. If you are watching the recording, you should try to go to that as well.
It's, I think technically you have to be a maintainer, but I've definitely sponsored, active participants in the community, to get them in, and it's a great… it's more of, like, a hallway conversation stuff, so, especially if you're listening to the call and you're an active, Participant, just ping us, and we'll see about getting you in.
Cool.
Well, I think if that's the case, we could probably end the meeting early here.
Thanks, everyone, for joining. We will resume in a week, otherwise, see you all, asynchronously, or in that PR, for the week tomorrow. Bye, everyone.
**Pellared** 25:12 Bye, everyone.
