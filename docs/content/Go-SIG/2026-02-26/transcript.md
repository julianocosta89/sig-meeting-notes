SIG: Go SIG
Date: 2026-02-26
Duration: 35 minutes
============================================================

## Zoom Recording Transcript

**Tyler** 02:02 Hey, David.
**David Ashpole (dashpole)** 02:04 Good to see you.
**Tyler** 02:06 Yeah, how's it going?
**David Ashpole (dashpole)** 02:08 Doing well.
**Tyler** 02:09 Yeah.
I think it might just be us today.
**David Ashpole (dashpole)** 02:14 Oh, yeah?
**Tyler** 02:15 Yeah, Robert's not coming. Damien doesn't show up to these, and I think I heard that Sam is also on, vacation now?
See, Brian just joined, though.
**Bryan Boreham** 02:26 Aye.
**Tyler** 02:27 Hey!
**Bryan Boreham** 02:28 Sorry, I'm a couple of nights late.
**Tyler** 02:31 Oh, no worries. We were just saying that it's gonna probably be a light day today anyways, so… yeah.
Yeah, I guess, actually, if that's the case, then I can probably jump in here and start sharing, and we can go over the agenda. I don't know if there's actually too much relevant To the audience here, but, get it on the… on the recording, at least.
Yeah, so go ahead and add your name to the attendees list if you haven't already. If you have agenda items you want to talk about, please go ahead and add them as well, and we'll jump in here. So, I wanted to talk about the next release. This is blocking other work that needs to get done at this point. I think we want to try to get this out.
The only thing that's really left is, these two PRs, as far as I've seen, Specifically, this PR here that complied with the W3C baggage.
Robert and I were talking about this beforehand, I'm not… exactly sure if we want to try to force this forward. David, I think you had some good Important, things to address here.
So, I think… Things is, I don't think Sam's gonna be here till next week. I do think that, like, committing things like this, is not… something that's a problem. Actually, I think all of Robert's suggestions aren't really… like, this is the default value, so I think we could probably just add these to the PR.
I don't know about this, this definitely needs, I think, some response, and I think this is a fair response.
Your point about it also being, like, correctly… set… downstream, after this function is being called, I think is also correct. I think BaggageDu does handle it, but… there's, there's definitely a hidden bug by keeping this. So if we start calling, I think, this function outside of, you know, baggage new or something like that, then, like.
**David Ashpole (dashpole)** 04:31 No, baggage.new is, like, the next line after this thing, right? So after the break, it calls baggage.new.
So, I… I'm not concerned… In that sense, it's more… I was trying to figure out In theory, this is some sort of OOM protection or something, right?
I wasn't sure if the idea was that we wanted to… not parse more than max members or something, or… Where's my base?
**Tyler** 05:09 Mmm, I see what you're saying.
**David Ashpole (dashpole)** 05:11 It's, like, it's… it's probably fine if we pass more than…
**Tyler** 05:16 So you're saying, like, do the comparison up here?
**Bryan Boreham** 05:23 So you'd just truncate it, wouldn't you?
At the break, because, like, you've added the dot dot dot, so you could have added 10 things.
And you've gone 3 over.
That's your point.
**David Ashpole (dashpole)** 05:36 I don't think it actually matters, honestly, as long as it gets handled down below. I didn't think it through, it was more just, like.
I wasn't sure if… it felt odd to do something that results in you going over the max, from, like, a code reading perspective, because I would never expect… have more than whatever the max number is, right?
**Tyler** 06:00 Yeah, and that was… that was kind of my point, though, is, like, if, if someone comes along and they're… they're reading this, and they think, like, You know, this function at this point should have, at most, max members, and it doesn't, as I start adding code here that expects that to be the case? You know, is there an inherent bug that could come out of that?
**David Ashpole (dashpole)** 06:23 Yeah, I feel like… Hmm.
Yeah, I would prefer if this is addressed. I guess… it feels like something that could be addressed in a small follow-up PR.
And I would be comfortable with that.
Like, I don't think the current code has a bug, if that makes sense.
**Tyler** 06:43 Okay, that was my same take on this, yeah.
**David Ashpole (dashpole)** 06:45 Good.
**Tyler** 06:46 is that maybe… maybe we can create an issue to track this, or if you wanted to, submit just a PR for this, and… Actually, I don't even know if it needs to get in before this next release, right? So…
**David Ashpole (dashpole)** 06:59 It's just like… Honestly, someone could take probably a… assuming Robert's comments are also non-blocking in a similar way, someone could just take all of these and open a small PR.
**Tyler** 07:11 Yeah, this.
**David Ashpole (dashpole)** 07:13 and whatever.
**Tyler** 07:14 Why not take it, always?
I don't… yeah, I don't think this is blocking either.
Honestly.
We could also just test this. The other ones are definitely not blocking. I think this is just… Code cleanup that is nice for… I think these can get merged to this PR, to be honest. I'm fine adding these to a suggestion.
So I think that seems fair. I think if Sam comes back and is like, we shouldn't have added this period at the end of the sentence, then… I think Sam's willing to… Open up PR for that, I guess I can speak for him there, but .
**David Ashpole (dashpole)** 07:52 It's a release blocking period.
**Tyler** 07:54 Yeah, right.
So yeah, I think, I think maybe just keeping track of this in an issue is to follow up, or maybe just ask Sam what they think And, yeah, we can do that.
So, yeah, why don't we do that? Why don't we try to create an issue after this meeting, and then, I think… Take another review on this, and then maybe try to get this merged today, probably tomorrow, and then get the release out, hopefully sooner rather than later.
Also, if others have… Brian, if you wanted to take a look at this PR, more eyes on this would be great. This is trying to address a…
**Bryan Boreham** 08:30 Yeah, I've read through it, I just didn't have anything to add. Oh, okay.
**Tyler** 08:35 Yep.
**Bryan Boreham** 08:36 I mean, it was… somewhat of a surprise that there were all these different limits.
**Tyler** 08:43 Yeah, this was created before the baggage spec actually stabilized, so…
**Bryan Boreham** 08:47 Okay.
**Tyler** 08:47 Got a lot of… Oh, there, yeah.
**Bryan Boreham** 08:51 Yeah, I mean, I guess messaging it to those people who are… have, like, 90 kilobyte baggage, And are gonna be surprised. But that's not really part of the PR.
Yeah, I, I, yeah, I've read it. I mean, do you want me to, like, approve it or something, or is that hopeful, or…
**Tyler** 09:14 Yeah, approving always is helpful, yeah. Like, any, like, even if your checkbox or checkmark is not green, like, we approve, we appreciate all that, like, you're a known figure in this community, so I don't think that there's any, we would appreciate it, yeah.
If you don't want to, and that's too much as well, like, we're not forcing.
But yeah, we would love any feedback that you have, and then we'll try to get this merged.
Similarly, I think there's this other PR from David, that it looks good, it's just documentation PR is, at this point, it's been litigated quite a lot, so… I think that this is one… it just needs another review from a not, Splunker at this point, so… Damian, if you're watching this, Who else? Flc, I think is on vacation, so… actually, yeah.
I guess we… well, don't we count, like, the author as being, you know, separate…
**David Ashpole (dashpole)** 10:12 I proposed that at one point, I don't remember if we updated the policy.
I don't think… It feels a little self-interested to now claim.
**Tyler** 10:22 I'm the one bringing it up. I'm pretty sure that that was our takeaway on that. I kind of feel like we consider… The author being an approver also as a separate entity, yeah.
**David Ashpole (dashpole)** 10:35 If you open the policy change.
Robert and I can approve it.
**Tyler** 10:40 Yeah, that counts, right?
Okay, I'll… let me double-check on that after the meeting, and then if it isn't there, then I think we definitely want to, because we run into these situations all the time, so, yeah.
**David Ashpole (dashpole)** 10:52 I don't know if this should be release blocking, like, I don't think… Actually, it's interesting, does Godox pull from head, or does it pull from releases?
**Tyler** 11:02 It's the releases.
**David Ashpole (dashpole)** 11:03 Okay.
That's a good thing.
**Tyler** 11:06 Yeah.
So, yeah, you're right, it isn't blocking. So I guess if we get the other one merged and we're waiting on this, then we can just move it to the next, release, that's not a problem.
Okay, well, if that's the case, then I will… we'll try to move this forward. I will take the action item, get another review on here to… Actually, David, could you take the action item to maybe create an issue in… for these, remaining tasks, and and then try to get another review in? I think Robert's… Your three comments, and then this testing one, and then all the other ones, I think, just get merged in.
**David Ashpole (dashpole)** 11:44 So the current policy is, at least one of the qualified approvals needs to be from an approver maintainer affiliated with a different company than the author of the PR.
**Tyler** 11:56 Yeah… I feel like we changed that, but nobody ever actually made it official.
**David Ashpole (dashpole)** 12:00 That's… that's correct. So now it's… it's just the… at least one reviewer… Needs to be from a different company, so you and I are from a different company.
**Tyler** 12:10 Yeah, great.
Sorry, I misled.
**David Ashpole (dashpole)** 12:13 We did make the change, so we're…
**Tyler** 12:15 So I think this is actually ready to get merged, so I actually think we could, why don't we just merge it?
**David Ashpole (dashpole)** 12:21 Yep.
**Tyler** 12:23 Cool.
**David Ashpole (dashpole)** 12:24 Oh, before you hit the button, I wanted to say one thing.
I do kind of wish we could document just the interface types and not every method.
But that's not what the spec says, and I don't want to go back and change the spec, and I think this is fine.
Like, reading through it.
**Tyler** 12:43 Yeah, no, that's a good point. Like, it's gonna read really poorly on the.
**David Ashpole (dashpole)** 12:48 Everyone who goes and looks at the package docs.
**Tyler** 12:51 Yeah.
Well, there's nothing stopping us from saying, Additional documentation here.
Like, on the interface documentation, you could also add, like.
**David Ashpole (dashpole)** 13:01 It's more that, like, one, it clutters up the actual functions that nobody ever… that people actually look at. But maybe it's a good thing, maybe not, and two, I… The one thing about putting it on the interface definition is you can say, like, all functions need to be safe to be called concurrently, or something like that, which implies, like, with each other as well.
**Tyler** 13:22 Hmm.
**David Ashpole (dashpole)** 13:23 It's kind of ambiguous if I can call, like, new counter and new histogram at the same time or something.
**Tyler** 13:28 Right. But I…
**David Ashpole (dashpole)** 13:29 Everybody, I think, knows what it means, right?
**Tyler** 13:32 Okay.
**David Ashpole (dashpole)** 13:33 But, I still think this is correct. I just wanted to, like, Anyone else felt strongly, like.
We could.
**Tyler** 13:41 3… This looks like it's… Oh, oh, sorry, Trace Pure. Oh, yeah, okay, sorry. Yeah.
Yeah, I… I… I would be in favor of doing what you just described, because… I definitely, when I go read the docs in my editor or in the package site, like, I rarely will read docs that are, like, in that, like, blown-out thing for the methods, so, like, I would miss this if it were just me. But we don't have to add it to this PR, and we can follow up on that.
**David Ashpole (dashpole)** 14:12 Yeah.
Yeah, that's fine. I think just getting it on there, fixing… marking the issue fixed, closing that chapter, whatever, it's like… Cool. Nice tweet done, yep.
**Tyler** 14:23 Let's, let's do that then. Let's, let's merge.
Okay, cool.
Alright.
Then, last off, Robert wanted to give an update on his vision for how he's gonna try to migrate new attribute types for the complex types, as well as this log API and migrate to that.
He's created a few milestones. He wants to add support for the empty, bytes and slice types in 142.
Wants to add support for the map type.
It is the hardest to implement and review because of the serialization and duplication logic.
In 143, and then in 144, he wants to change the logs, API, and SDK to use the attribute package and remove the log key value.
Yeah, I guess my only feedback is that… would be nice to have these in the same release, but I can understand if there's, like.
Developer capacity here that we're missing, where we can't get all of this reviewed in one release, then it's fine breaking it across the two.
**David Ashpole (dashpole)** 15:30 It's… I think these are reasonable goals.
I would probably, yeah, say the same thing, like.
Put them all in, like, a milestone for 42.
**Tyler** 15:40 Yeah.
**David Ashpole (dashpole)** 15:40 And then… Wait till they're all done, and then… Change the logs API and SDK.
But the ordering's correct.
**Tyler** 15:49 Yeah, that makes sense to me.
**David Ashpole (dashpole)** 15:53 For some reason, I thought we supported bytes, but, like, as string or something.
**Tyler** 15:58 Yeah, I mean, technically, you can always create a… Quite slices of string, but .
**David Ashpole (dashpole)** 16:05 It needs to be separate, yeah.
**Tyler** 16:06 Yeah, it needs to be separate, because we need to be able to, like, deserialize into OTLP, and we don't… there's no way to… like, we don't understand the distinction at this point for that, yeah.
**David Ashpole (dashpole)** 16:16 Now I can finally put a byte slice as a label value in my Prometheus metrics.
**Tyler** 16:22 Yeah, and then we're gonna cut it off at some arbitrary limit, and Yeah, you're gonna… you're gonna be… Very confused why your byte size isn't deserializing on the other end.
Sorry, bad joke. Okay, cool.
That is the end of the written agenda.
Any other topics people wanted to talk about? Cool projects they're working on?
**David Ashpole (dashpole)** 16:50 Ryan, are you interested in exemplars and truncation at all?
**Bryan Boreham** 16:56 I'm a little bit interested in exemplars, that was the first thing I put live when I started at Grafana Labs.
**David Ashpole (dashpole)** 17:04 Okay, fun. I… I'll raise one topic, just because you're here, and it's the three of us.
So this is about the Prometheus exporter. Today, the Prometheus exporter just maps exemplars to Prometheus ones.
But if you do anything other than trace ID and span ID, you almost always exceed the 128 Roon limit of open metrics, and I think… I think it just gets dropped.
I was trying to read the code, and it looked like it panicked, but the issue that someone raised says that it just gets dropped. So I'm… I'm figuring out… I'm trying to figure out how to fix it.
And one of the interesting, like, wrenches is that Open Metrics 2, we're planning to remove the exemplar limit.
And… Implement exemplar limits similar to label limits.
By implementing it server-side.
And so having that be, like, a thing that the server decides, in terms of how many… Exemplar runes, or whatever it wants to accept.
And how it wants to deal with ones that are longer than that.
So there's a… there's a PR in… Let's see…
**Bryan Boreham** 18:28 I agree that the… The limit is way too low. I think it was originally implemented as 64, even though the spec said 128, and that caused… Quite a lot of angst.
But, yeah, Google.
**David Ashpole (dashpole)** 18:47 Let me just drop some links.
So here's… here's the original… Hotel Go PR, and… I think there's a corresponding issue.
**Bryan Boreham** 19:06 Yeah, limiting it to Rune's characters is also stupid.
**David Ashpole (dashpole)** 19:10 That was… Yeah, yeah, no, it was very… Shoot, sorry, too many times.
Cheer.
So there's the PR, here's the issue.
I think the more interesting question is.
my first reaction was that I actually think the… Prometheus Client.
Should… Deal with exemplars that are too long, more gracefully.
Rather than putting it here, because… the OpenTelemetry client has no idea what Stuff is being negotiated.
And so I also opened an issue in… the Prometheus Client Go repo.
Which is maybe… Let's see, where's the best place to start? I think I can share my screen, let's see.
window.
Right, so this is actually pretty old. It's almost a year old now, but basically it's pretty easy just to, if you do any filtering on your metrics, to blow way past the The exemplar rune limit, right? And today, I think, they… Is also this issue.
That was closed, I think.
Oh, but he closed it himself.
So… basically asking for it to be relaxed. Now there's a plan for relaxing it, so I opened this issue here.
To explore that?
My preferred solution would be if the Prometheus client stopped Dropping them and started truncating them.
it gave us some way to make sure that the trace ID and span ID could be kept. And then eventually, when Open Metrics 2.0 lands.
Then they can stop truncating them at all, and just send them out.
I think, alternatively, we could accept this PR that this person has opened, that just… pre-truncates them before the exemplar is handed to the Prometheus client.
So that it fixes the issue for now.
The only question then is, like, how do we remove that behavior once… there is a viable path with the Prometheus client.
**Bryan Boreham** 21:57 Yeah, so… Very high-level, the exemplars are… in… in Prometheus are not… like, conceptually tied to traces. That's the most popular way that people use them. So I would definitely… I mean, you know, it would be pragmatic for that library to do something special for traces, but not… spiritually pure.
To have it truncate. So, in terms of the truncate by ordering… Labels are always ordered by… well, unless that API is weird, they're always ordered alphabetically.
So that… Leaves you with a kind of an ugly… thing, to try and, like, keep the first N.
So… So we could have a… like an API saying these are the ones that, you know, this is the order I want you to drop them in, or something like that. That sounds just about possible.
**David Ashpole (dashpole)** 23:04 Oh, no, it's, yeah, yeah, so this is… The Prometheus Client Labels implementation is actually just a map.
**Bryan Boreham** 23:11 Oh, okay.
**David Ashpole (dashpole)** 23:12 Server one.
**Bryan Boreham** 23:13 Well, either way, you can't… you can't use the ordering.
Yeah, I don't know, I'm not kind of immediately going past this. The… exemplars.
the labels that you attach to exemplars in… from inside… from Prometheus data model point of view, don't need to have anything to do with traces.
I mean, I can kind of add some color from what actually happened once we put this thing live.
Broadly speaking, nobody used it.
I mean, yeah, I haven't gone and queried the stats, but it… One thing I do know is that we were very sensitive to the amount of memory this thing might take up, because the Prometheus implementation is actually completely in memory.
And, that was the thing we were very sensitive about, and I do know for certain that you can turn it off completely and see no difference in our production memory usage.
So… so the one thing that we were really, really sensitive about was… Love it.
Never, never.
**David Ashpole (dashpole)** 24:42 I mean, so…
**Bryan Boreham** 24:42 Listen.
**David Ashpole (dashpole)** 24:44 And that's just… was that the client side, or was that… I assume…
**Bryan Boreham** 24:47 first, like, no.
**David Ashpole (dashpole)** 24:48 Yeah, the client doesn't…
**Bryan Boreham** 24:51 Well, I suppose any one client is storing the last exemplar for everything in memory, so yes, there's same… same concern, client-side, but I'm talking about servers that hold a million of these things.
and, relatively speaking, it's… it's a… it's not visible.
So, however, I mean, I… you know, if you… if you just said, let's have no limit whatsoever, anywhere, then somebody is going to show up and put a, again, a 90 kilobyte string in this thing, and And spoil the party for everyone.
**David Ashpole (dashpole)** 25:32 I think that… At least in the open metrics group, the idea was that we would before we implemented OpenMetrics 2.0 in the Prometheus server.
we would introduce a… an exemplar limit that defaulted to whatever Open Metrics 1 did.
So, more that… I think there's a few… Weird bits, maybe, which is that… Currently, if you try and record an invalid exemplar, it just gets ignored.
And now you'll try and send an invalid exemplar, and it'll get dropped server-side, which is a bit worse, because if you just ignore a bunch of ones that are invalid, you still end up sending a valid one at the end of the day, most of the time, probably.
Right?
**Bryan Boreham** 26:21 Yeah, well, we also have…
**David Ashpole (dashpole)** 26:22 Excluded.
**Bryan Boreham** 26:23 We have the option to truncate server-side.
you know, keep the first 2K, or whatever.
I, again… Yeah, we need… we need this thing about ordering I mean, we kind of have more flexibility No, we don't really… it's kind of the same, yeah, so… so in the client library, you would have to… somehow convey your desires as to what you felt was more important, which is the trace ID and span ID. You'd have to have some kind of… side channel to convey that, and it's a little bit ugly. Whereas in the server, it can just be in the config. Say, look, this is my server, I want… when you see an exemplar that's too big.
I want you to prioritize the span ID and trace ID, and that's perfectly legitimate config for a server. I'm just saying, kind of.
hard-coding trace ID and span ID into the Data model of the code.
Makes me uneasy.
But having the concept of truncation, having the concept of prioritization.
And having that configurable server-side is all perfectly fine.
toe.
and, you know, it's, it's… So, the most popular… wildly too long label for people to send us is a Java class path, currently. You know, not in exemplars, but just in metrics in general, or, you know, as a resource attribute.
People regularly send us I don't know if they're 90K, I'm just pulling that number out of the air, but certainly more than 2K class paths.
and, and we had to move from just throwing, you know, rejecting that as being… Too long to… truncating it as being too long.
So… Yeah, I guess… I guess the… that's sort of the worst that I can imagine, is that people will start putting the Java class path in their exemplars.
And, we'll have to truncate it.
**David Ashpole (dashpole)** 28:51 I assume we would just… I think the current… PR that's open in Hotel Go.
just drops both the key and the value if it can't fit. Like, it keeps whole.
Labels.
**Bryan Boreham** 29:04 Huh.
**David Ashpole (dashpole)** 29:05 So we probably wouldn't end up truncating the values, we would just… you'd be missing some.
**Bryan Boreham** 29:11 Yeah, no, understood.
**David Ashpole (dashpole)** 29:12 And just keep… The trace ID and span ID.
**Bryan Boreham** 29:21 So that's in a context where you know that you prefer trace ID and span ID.
**David Ashpole (dashpole)** 29:26 Yes, so one… one thing that's nice about the… Hotel Go solution is that We can be opinionated about.
the behavior when it drops. Yeah.
**Bryan Boreham** 29:40 Okay. It probably means we never get rid of it, or we make it, like, configurable someday.
**David Ashpole (dashpole)** 29:45 So people that really know what they're doing can, like, remove all the limits across their clients and across their server, and bump it above 128. But… It feels… I would be kind of sad if 6 years from now, everyone is still… Limited to 128 characters, effectively.
part ruins.
**Bryan Boreham** 30:10 Yeah, don't… don't limit it on wounds, it's fucking stupid.
**David Ashpole (dashpole)** 30:18 Cool, I… I wasn't looking to get anything out of it other than your thoughts, so thank you.
**Bryan Boreham** 30:25 Good luck.
**David Ashpole (dashpole)** 30:27 Leave it.
Well, I think that's it, Tyler.
**Tyler** 30:31 Yeah, cool. No, yeah, absolutely.
**David Ashpole (dashpole)** 30:33 you're interested in contributing to the Prometheus exemplar.
Versus hotel discussion.
**Tyler** 30:41 I… I'm very apt to getting nerd tonight by that, but I need to refrain, because I have some… No, you… you do…
**David Ashpole (dashpole)** 30:47 You do cool stuff. Go work on OBI. We needed to do all sorts of other cool things.
**Tyler** 30:53 Yeah, right, yeah.
Yeah, cool. No, I'm super supportive of what you guys just said. That looks great, yeah.
Awesome. Well, Cooley, if there's nothing else, we could probably end it here.
Yeah.
Cool. Alright, thanks guys. Talk to you later. Bye.
**Bryan Boreham** 31:12 Thank you, bye.
