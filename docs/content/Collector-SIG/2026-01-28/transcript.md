SIG: Collector SIG
Date: 2026-01-28
Duration: 62 minutes
Zoom Recording URL: https://zoom.us/rec/share/7eYYz_ffgAvUPUzymdl18c4gZIuzZup4NFE6Mg_fawLE63r0zar2XozebRTRUgtt.81ioPh0o-sJ3wnYj
============================================================

## Zoom Recording Transcript

**Perk (Marcin Stożek) | Elastic Ingest** 04:31 Hey, Earl, how are ya?
**Andrzej Stencel** 04:34 Hello.
Anybody want to say anything for the first topic?
**Evan Bradley** 05:17 I don't have anything.
**Andrzej Stencel** 05:35 Maybe, Evan, you should start with your…
**Evan Bradley** 05:38 Okay, so I'm doing a little bit of… Just kind of performance testing on the file storage extension, or just storage extensions in general?
So I was doing a little bit of, just digging through the… what do you call it, the issue tracker, and, found that somebody did some testing that found that the database storage extension, running with a SQLite backend.
Was apparently more performant than the file storage extension, and so wanted to… Check and see if anybody had any, like, input or advice or anything on… Whether they've, they've seen similar, performance, characteristics.
Or, any advice… so I'm gonna go through and test this and confirm it, and I would potentially like to alter what we suggest as a default.
Storage extension, depending on the results. So I was just looking for some input on that, if anybody else has, worked with this topic.
**Mikołaj Świątek** 06:50 In that… in that very issue, I actually tried to reproduce this and failed.
So it's not that trivial. I also wrote down, there's a pretty long comment by me, how I think… what you think I should do, what I think you should do.
In order to try and, reproduce this problem. Part of this part of the, I suppose, complexity of this specific situation is that it has to also do with What happens if the OS page cache is clear?
So, it's not that easy to just write the benchmark, right? Because you have to go and write some stuff in there, stop, then clear the page cache, ensure that it's clear, and then… You can… you can actually try… try reproducing the behavior discussed in there. Like, it's… this is actually in my backlog somewhere, but it's pretty low, because it looks like… high, high effort to actually reproduce what's good and to figure out what's actually going on. But if you want to have a stab at it, that would be great.
**Evan Bradley** 08:08 Okay, cool. I might reach out to you at some point later, if that's alright, but thank you for the update. Obviously that was in July of last year, so, if there's been no further changes, then it's good to, just kind of know what the current state is.
**dpaasman** 08:28 I want to throw out there that, so, at BinePlan, we have an engineer that, he's been looking at this problem, because in our production experience, we've definitely noticed issues with the file storage extension.
And so we've actually made two new different kinds of storage extensions that we have in our distro. One of them uses the uses Pebble, which is a key-value database written in Go, and then the other uses… let me check what it is. Badger. Badger, which is also a database written in Go.
Or key-value database written in Go.
So we've written both those extensions, and we've seen… better performance out of both of those. So I can get you in touch with our engineer that was working on that, and he can kind of talk to you about the testing that he's done, and Performance improvements that you've seen?
I think this is something that eventually we want to try and upstream.
to contribib as well.
we just, you know, this is very fresh for us yet, so still just working on getting some numbers around it all. Yeah, I can connect you with them if that's something you'd be interested in.
**Evan Bradley** 09:45 Yeah, for sure, thank you, and thanks for the information.
Yeah, let's talk about that offline later and, see what we can do.
**dpaasman** 09:53 Sounds good.
**Evan Bradley** 10:03 Okay, if there's nothing from anyone else on the call, you, know where to find me, or feel free to put a comment on that issue.
Andre, you have the next item.
**Andrzej Stencel** 10:16 Okay, thanks. This is just a courtesy for Andrew Wilkins. I think Andrew discussed this with me today.
who's not here today? The RFC for scrape Control Extension.
I think I'm sharing the screen.
So Andrew created this RFC, and he's… Looking forward to your comments.
It basically, from what I've read, I haven't gone very deep into it, but the scraper controller is the thing that is behind closed metrics receiver, and a couple other receivers. I don't know, SQL query receiver comes to mind, probably many others.
And you're… you can only, like, use time-based, scraping.
And Andrew wants to extend that to be able to register an actual Collector extension that is able to trigger this scraper based on Something. Maybe based on the webhook, maybe based on something else.
So if you're interested, take a look.
And I think that's it. Now I need to find my zone controls.
At a loss.
How do I stop sharing?
It's fun.
**Fairly OddParents (ca-wat-brt3)** 12:03 I think I'm next, is that right?
Looks like it.
I'm just… What's… broadcasting the prototype that I've started, for using Weaver.
Through the test containers package in a Go test. Something… it's an API that I'm hoping receivers can start to use when they make SEMCOMF transition to validate that they are actually in adherence with whichever SemConf version they are currently trying to test against.
It's not super far, but I decided to post it to get people's opinions, because I'm not sure if necessarily everyone's going to agree with the approach, or if anybody has a better idea or different opinions. I decided to Just post at least something that showed it would work, and… looking for more collaborators. I think Ariana's on the call and already mentioned that they were interested, so that's good.
**ariannavespri** 13:03 Anybody else?
**Fairly OddParents (ca-wat-brt3)** 13:04 Has opinions, feel free.
I believe that's everything for me. If there's no comments, Yatsen can have the floor.
**ariannavespri** 13:55 I don't know, maybe we should just think about how to collaborate with, on this, like, maybe, Hash out some action items for the things that you were mentioning are still to be done, so that we can coordinate the work.
Either the two of us, or, you know, if anybody else is also interested.
I mean, I had a look at it, and I read your comments, and I kind of made myself an idea of what are the pain points that you were, like, expressing, and what could be done there.
Or, you know, just, like, a vague idea, so, you know, as I said, I would be very happy to collaborate on this, so let's just, I don't know, sync either on the PR or… I mean, I'm on… of course, I'm in the CNCF Slack, so…
**Fairly OddParents (ca-wat-brt3)** 14:43 Sure. Whatever you think is best.
Yeah, I'll start with a Slack DM. If anybody else wants to be part of that, let me know.
Most of what I was thinking I mentioned on the comment, there's a couple other things that I was thinking about that I haven't written down yet, and so I can start to figure out… what… what vehicle to use to collaborate on it, either on a… either… I commit a skeleton of this package that we start adding into, or something like that. We can figure that out.
**ariannavespri** 15:12 Sure.
**Fairly OddParents (ca-wat-brt3)** 15:33 Joten, if your mic is still not working, maybe we could skip ahead to the next piece and come back.
**Yaten Dhingra** 15:38 Like, audible.
**Fairly OddParents (ca-wat-brt3)** 15:40 Oh, yep.
**Yaten Dhingra** 15:42 Yeah, so I just wanted to discuss on this issue that, like, if we, check in the collector contract repos.
There are some PRs which are merged, and there are some issues which are still open, which were created by the issue generator.
as a result of the failing CI test.
So, as of now, even if the PR gets merged, there is, No method of closing that particular issue.
Which was created by those CI, CI checks.
So, my proposal was to, can we have something like… We can change the issue generator so that if a PR is merged, all the corresponding issues which were created as a result of the CI checks Those are also closed.
Cool.
**Jade Guiton** 16:40 I… so this issue here was because of failing tests on main.
That were attributed to the PR, I believe.
So they're not… I'm not really sure I understand why it needs to be closed automatically.
Has the… has the failure been… Fixed?
**Yaten Dhingra** 17:14 Yeah, so basically, I have attached a sample PR under an issue in the In August.
In the Google Doc. So basically, if we, check the… check that PR, it is merged, and the issue is still open.
So, those issues are not getting, closed automatically.
**Jade Guiton** 17:32 But… so I… if I'm not mistaken here, the issue was created as a response to the PR being merged. The PR was merged, the commit was added to main, CI failed on main.
And then the issue was filed, attributing the failure to the change in that PR.
**Yaten Dhingra** 17:52 Yes, exactly.
**Jade Guiton** 17:54 So it wouldn't make sense to close the PR until the… Code owners have taken a look at it and filed another PR to fix the issue.
If there is an issue, of course, it could be a flaky test.
**Yaten Dhingra** 18:10 Oh, sorry, I didn't get your point. Could you kindly re-elaborate a bit more on this?
**Jade Guiton** 18:16 Yes, so, let me check the timestamps.
The PR was merged January 12th, 823.
Yeah, and the… Issue was opened an hour later.
The issue was opened because there was a bug in that merged PR.
Which causes the tests to fail.
**Yaten Dhingra** 18:43 Yes.
**Jade Guiton** 18:44 At least, presumably, the bug is in that PR.
Yes. So, for the issue to be… closed.
the bug needs to be fixed, the test needs to be fixed in a separate PR.
I'm not sure if, like, a second PR could be filed… in a way that, like, if you mention fixes an issue, yeah, that should probably close the issue automatically, I think.
But, yeah, it would have to be a second PR that fixes the issue in the first PR.
Does that make sense to you?
**Yaten Dhingra** 19:22 Yeah, so basically, the… another PR has to be opened. What I have understood is.
another PR has to be opened, so that The failure check can be passed, and then that corresponding issue will be closed, right?
**Jade Guiton** 19:39 I'm sorry, I don't think I understood, but… To explain in a different way.
The original PR probably had a bug.
Oh, wait, so the…
**Yaten Dhingra** 19:52 Thank you.
**Jade Guiton** 19:53 The original PR was for fixing… A flaky test, I didn't see that.
**Fairly OddParents (ca-wat-brt3)** 19:59 But it was in a different receiver.
The attribution could be wrong, like, it could be that something else broke it, but the issue generator decided to attribute it to that one, I'm not sure.
Or the test was flaky, and it's just the most recently merged change after the flake.
But… Regardless, I don't think there is any case in what's brought up here where anything should have been auto-closed and wasn't.
**Jade Guiton** 20:28 Yeah, I think the attribution to PRs is just based on the latest PR that was merged when the flick occurred on Maine. So, yeah, it's likely that this is just a flaky test unrelated to that PR.
But yeah, the… yeah, here the code owners would need to… from the… of the SOLUS receiver, would have to take a look.
Before it could be closed.
**Yaten Dhingra** 20:58 Yeah, okay, okay, I got your point. Actually, I didn't know that another PR has to be came up with so that in order to close the particular open issue, as a result of the failing CI check.
I'll research on this, more today.
I didn't go deep into this, so yeah, maybe then we can discuss about this.
**Jade Guiton** 21:22 Yeah, to be clear, like, the issue gets filed not when the PRCI fails. When the PRCI fails, that stays within the PR.
The issue is only filed if CI fails on something that was merged into main.
So… Yeah, I don't think it's… Related.
**Yaten Dhingra** 21:43 Yes, yes, yes, I got your point. Actually, I was thinking that a PR was… the issue was generated because a PR, a CI check failed.
So, yeah.
**Jade Guiton** 21:53 Right.
**Yaten Dhingra** 21:54 Cool.
**Jade Guiton** 21:56 Okay, that makes sense.
**Yaten Dhingra** 21:59 Thank you.
**Jade Guiton** 22:03 Pablo, do you want to take the next point?
**Pablo Baeyens** 22:07 Yeah, so… We were having a discussion about this PR on the CAdvisor repository among containers and approvers, I was asked to bring this up to the governance committee to see… Who should take… care of this discussion, from the OpenTeunetry side.
There seems to be… agreement that the collector seat can… Owen the conversation?
So I wanted to bring it here, and I guess… either Bradon or maybe David, you can feel us all with the context of this?
**David Ashpole (dashpole)** 22:55 I'm happy to provide context. So, let's see.
like, 10 years ago, started as the maintainer of CAdvisor, and I maintained it for, I think, 4 or 5 years, so… I know a good bit of the history. I'll give a really abridged version, I promise.
Which is that… The kubelet never wanted to be in the business.
Of providing container metrics.
But… a lot of users needed them, and so it did. And the plan was always to rip it out. Like, oh yeah, something else will come along, it'll be better, it'll collect really detailed container metrics in a really configurable way, and users will be able to own their own container monitoring story. But that never really happened.
And so… CAdvisor has been built into the kubelet for a long, long time. There are a few issues with it. One is that it only supports a specific list of container runtimes, so we have this nice container runtime interface, but you lose your container metrics if you don't use, like, Docker or ContainerD or, whatever Red Hat's one is, right?
It also only works on Linux, so… Windows, I guess, can go write their own library and build it into the kubelet. Doesn't work with GVisor or… Firecracker, or whatever the other ones are. So, it's… it has some limitations, but it's also extremely widely used and widely popular.
And… what Sig Node would like is they would like to just own collecting the metrics from the CRI that are required for Kubernetes control loops.
doing eviction, doing auto-scaling, you know, with CPU and memory and such, and they don't want to own the rest of the metrics. And so.
They're looking for other communities that are willing to take the mantle of We do container monitoring.
And… donate the C-Advisor project in some form, or at least have some replacement with a migration story. So I think the ask From my understanding, for us, would be, one, do we want to a drop-in replacement.
I don't think that's necessarily mandatory, or two, Do we want to have… Other alternatives.
For receivers, for container monitoring.
And provide a migration guide.
Or do we think that the existing collector receivers are already a good replacement for CAdvisor, and do we want to help the existing users of the C Advisor endpoint migrate to the OpenTelemetry collector? So I think those are maybe, like.
A flavor of some of the things we could choose to do.
I'm happy to answer any questions that people have as well.
**Pablo Baeyens** 25:55 When… when you talk about donating… something… does that also mean the people currently maintaining that on the CAdvisor side would… Come and join us to maintain that?
**David Ashpole (dashpole)** 26:11 So, let's see, there are a few maintainers outside of Google, mostly from one other company, and they… I don't think… I haven't talked to them specifically, I don't think they're interested in, like… joining collector meetings, and I think they use C-Advisor the way it is. I would guess they're more likely to simply fork it and continue using it, and they're not… you know, if we gave them a hard… a difficult migration, that I don't know if they would move.
Then… the… the other Google maintainers, are extremely… lightly involved in C-Advisor. You know, we do dependency bumps, review PRs occasionally.
And occasionally someone asks, the SIG, the Kubernetes node SIG.
for additional config knobs, or additional metrics, or things like that. But… so the answer, in short, is I don't think there's any maintainers coming along with this.
The reason they're donating it is because of a lack of maintainership.
And because they would like to be able to remove the C-Advisor metrics.
The really rich, detailed ones from the kubelet.
**Pablo Baeyens** 27:39 I see. Okay.
**David Ashpole (dashpole)** 27:43 So maybe an unusual donation request.
**Pablo Baeyens** 27:46 Right.
**Andrzej Stencel** 27:50 Take it, we don't want it by donation.
**David Ashpole (dashpole)** 27:55 I think it's more, like, up for grabs if anyone wants to own this space. In theory, I understand why they came to us.
Us being open telemetry in the collector's sake, because, like… basic container monitoring seems like a reasonably good fit, but I agree that there's a lot of questions about who and what and when.
And what it looks like.
**Pablo Baeyens** 28:19 And do you or anybody else in the call know what the… GOP is, To see Advisor on what we currently offer for container monitoring.
Like, is there a lot of work to be done to make sure that we provide the same that CAdvisor provides? I have no idea.
**Fairly OddParents (ca-wat-brt3)** 28:44 There is some work. I did a, like, a comparison.
we have the Docker stats receiver.
It actually gets almost the exact same set of metrics.
But it will only work for Docker, because it uses the Docker API, it doesn't use the CRI, it doesn't use… any… any more generic API to do that, so… there's probably work to make it so that it would work for other container runtimes, because right now it wouldn't. In terms of the stuff that CAdvisor's capable of collecting from the node.
Pretty much everything is either in-flight and host metrics are already capable.
But it's not going to be flavored as… oh, your Kubernetes node has XYZ thing, it's just, like, generic system metrics.
So… Probably either migration dock work or Samantha Conventions work to map it to… more familiar Kubernetes… Terminology and the metric names and stuff.
**David Ashpole (dashpole)** 29:49 Yeah, I… I think other container runtimes have some Prometheus endpoints as well.
But I'm not sure if those map one-to-one. I suspect they don't map one-to-one with the names, or… like… contents of the CAdvisor endpoint.
**Fairly OddParents (ca-wat-brt3)** 30:05 Probably not. I mean, the, the.
**David Ashpole (dashpole)** 30:08 example.
**Fairly OddParents (ca-wat-brt3)** 30:09 Yeah.
the… stats that the Docker stats receiver collects, Docker itself, I believe, gets those from standard cgroup statistics, so any container runtime that is also getting those same cgroup statistics will likely produce something similar, but it's also not… not guaranteed that they're going to instrument those in the same way, with the same naming scheme or semantics or anything, either.
**David Ashpole (dashpole)** 30:36 Yep.
I… right, I think… I think the most reasonable Outcome would be, if we can find people who are interested, would be To try and come up with Right, like, CAdvisor could become a collector-receiver, but we would likely rename everything to be OpenTelemetry Conventions. But I think that's only if we find people who are interested in owning it.
**Fairly OddParents (ca-wat-brt3)** 31:13 That's the big question.
Which…
**Pablo Baeyens** 31:20 I think it's fair to use DSCOL or the Collector Dev Channel to figure out if there are people willing to… Maintain this, or, like, be code owners?
That seems like the next thing to figure out.
**David Ashpole (dashpole)** 31:48 Do you think it would be helpful as a next step to open a… new component proposal, or is that premature? I just… if there's somewhere that we can post that we're looking for people who are interested.
It might be helpful.
Not sure what the right format of that is. Or if you want to go talk to the GC or do other.
**Pablo Baeyens** 32:10 We can figure it out on our own, I don't think we need to involve the GC.
like, we can open an issue, yeah, I think that's fair. There's no… specific components to be donated, only the idea of a component, but it's fine, it's an issue. We can discuss it on… On an issue, and whenever… We get, you know, people, we… Right on the component, and we do the donation process.
**Fairly OddParents (ca-wat-brt3)** 32:42 And that should be in the contributory bow, likely, right?
**Pablo Baeyens** 32:46 Right, yep.
I mean, my opinion, I'm not… I'm not the one that has to decide here, but, like, yeah.
If other people agree, yeah, I think that should be fine.
**Fairly OddParents (ca-wat-brt3)** 32:59 Okay.
**Pablo Baeyens** 33:26 I didn't write this down on the agenda, but I'm wondering if it would make sense to talk about the… issue, Brayden about… The configuration for enabling and disabling metrics on components.hub.
A migration, like the host metrics receiver?
**Fairly OddParents (ca-wat-brt3)** 33:49 Yes, the Oh, alright.
I don't know if we have anything… any new grand solution for this, but I can at least present the issue, because other components are probably going to run into this, too.
Basically, in Host Metrics Receiver, what we want to do is when the SEMCOM schema is ready and we start writing it, we have feature gates to control writing the old schema and writing the new schema.
With the ability to possibly write both, or not… or neither, I guess technically the functionality would allow you to do that, but anyways, The issue we're gonna run into is configuration, because… The only way for us to have these generated metric builder configs from mDataGen.
Working for two entirely separate schemas.
Is for them to be either in two different fields, one being metadata or, like, metrics old, or metrics legacy and metrics, or metrics new and metrics is the old one. Whichever direction you do it, either way, you're doomed to a breaking change when the old schema stops being written.
And the other option is maybe not even technically feasible, which is… to merge the two metric builder configs into one metrics field, but there's no guarantee that the same metric name won't appear in both schemas, like, something may not have changed when it moved to SEMCOM, so if you're referring to some process.whatever metric, are you referring… there might be ambiguity between whether you're referring to the old or the new one.
I still don't know how to solve this. I've been thinking about… what ways we can do it without a breaking change, it might just not be possible. It might… we might just be… be screwed, but if anybody has ideas.
Got it.
Feel free to comment here or on the PR.
**Pablo Baeyens** 36:24 Okay, thanks. I… I also can't think about any magical solution, but, like, yeah, maybe somebody… On this goal, thinks of it's something.
If… there are no other topics I was going to mention. If you were at the beginning of the… call on you… there was this, AI, bot on the call.
and you happen to be a European national and want to request your data for the TDPR, let me know on the DMs, and I can… send you a template of what to send to the company behind this AI bot.
Just to… make some noise, I guess, and let them know that we don't… One.
Those bots to be… Opt out.
And I think that's all.
Thank you, everybody.
**Fairly OddParents (ca-wat-brt3)** 37:30 Thanks, everyone.
**Pablo Baeyens** 37:31 U.
**Andrzej Stencel** 37:31 Thanks.
**Evan Bradley** 37:32 Bye, everyone.
**ariannavespri** 37:33 Thank you.
