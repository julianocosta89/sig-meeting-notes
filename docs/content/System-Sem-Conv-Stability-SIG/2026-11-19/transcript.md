SIG: System Sem Conv Stability SIG
Date: 2026-11-19
Duration: 30 minutes
============================================================

## Zoom Recording Transcript

**Pablo Baeyens (Datadog)** 02:54 Hey.
I was… keep going.
**Donal O'Sullivan** 03:02 Hey, guys.
**Christos Markou** 03:03 Hey there.
I would say good, not bad.
Some people mentioned, that probably not… Super attended, was not super crowded.
But I think, yeah, usually North American versions are… less crowded compared to European ones. I think more people than last year in Atlanta, from the maintainer side at least, were there.
So, at least for me, it was productive, I would say.
And, yeah.
Utah was also great. We did the road trip with… Edmo and Roger, 3 days before.
**Pablo Baeyens (Datadog)** 03:45 Oh, nice. Yeah, that must be nice. I… Regret not doing that when I was there for KubeCon. Yeah.
**Christos Markou** 03:53 I had exactly the same thoughts. Two years ago, I just went for KubeCon.
Know how to… To make it worth the distance.
Pablo, you are still the liaison for this group, right?
**Pablo Baeyens (Datadog)** 04:32 Yep.
**Christos Markou** 04:32 After the election, yeah, because on Cates, we… We changed, we got, Daniel, Dan Gomez Blanco.
Yeah, okay.
**Pablo Baeyens (Datadog)** 04:45 Yeah, I don't remember what… which ones Josh took, but not this one.
I guess just would make sense, since he knows about Semcom, but… Just the, semantic dimensions tooling, like Weber.
What's up?
Cool.
Did you discuss anything at KubeCon about… Post metrics, or…
**Christos Markou** 05:51 I don't remember… Anything in particular.
I think it was mentioned about the V1 of host metric receiver.
And I think… There is some consensus from multiple people that It's something that… We need to push, we can't push, so maybe that's the highest.
The most important thing right now.
Yeah, given that we have the… most of the metrics, most of the SMAT conventions, Donal, probably you can say more, you're planning to promote the metrics as well, to… to release content.
then I think all the work is… all the work that is missing is on the host metrics part.
But we need to maybe… just make it more scoped, and ensure that we can do it by KubeCon Europe.
**Pablo Baeyens (Datadog)** 06:51 Okay.
Cool.
I guess I'll mention… There's been some talk about creating a cloud semantic conventions, group.
I think Josh Surith would be involved, and then somebody from AWS, probably, as well.
I don't know if they would take a look at, like, the host.
Namespace, but maybe?
Yeah, but otherwise, it would be good for, like, the resource detection processor, I guess, even if it's not, like, system. It uses a lot of cloud conventions.
**Donal O'Sullivan** 08:09 Yeah, just to add on what Christos was saying, like, I was gonna open up a pull request in Semantic Conventions to, What, system metrics to release candidate.
And… Yeah, it's just, like, an FYI, I guess it's not… I'll just open the pull request. And then I know prior, we were discussing the V1 work required.
And I know you brought up a few issues, Pablo, so… I think there was one with the filter package, so I'm just working on… Changing the name of the filter package, I know there was an open issue that the name was too generic, so I'm gonna open a pull request for that, and gonna try and tackle, some other… Issues that are blocking, like, the, I guess there's probably… there's… I think there's 3 issues there in prior meeting notes of stuff that has to be done before we start looking at the V1.
Steps, you know, I think there's, like, configuration, testing, documentation, that kind of thing.
I had a quick look at the, configuration. I think, for the most part, everything is fine. There is… I just had a question around, Because I know the host metrics name changed from, like, host metrics, one word, to, like, host underscore metrics, and we still allow both, so you can, like, in your configuration, you can specify the deprecated name, or you can use the new name? Like, I guess to… if we're going V1, are we just going to remove the deprecated name altogether, if that makes sense? You know, from, like, the user's config?
Alright, Braydon.
**Pablo Baeyens (Datadog)** 09:38 I personally think it's fine to keep it, like, it's not a lot of work to maintain the Alias, and everybody's using the Alias. I don't know. Unless we change the configuration dramatically, and then, like.
doesn't matter much, I think it's fine to keep it.
**Donal O'Sullivan** 09:56 Yeah, that makes sense.
**Braydon Kains (Google LLC)** 09:57 Selfishly, I want to keep it. I will follow whatever the rules of the group are, but I've always kind of thought that the underscore separated naming effort hasn't felt worth it to me, and I would rather just keep the old one around forever, but… If… if… it comes to a point where we remove all the old aliases, then we can remove it, but I don't know if we necessarily have to for… 1.0.
**Donal O'Sullivan** 10:26 Yeah, makes sense.
That's cool. I'll leave it as is.
Braydon, you joined late, but I was just mentioning I'm gonna open a PR to… Push the system metrics to release candidate in semantic conventions.
Best on the road, right.
**Braydon Kains (Google LLC)** 10:45 I think so, yeah. I don't think there's anything else pending before we push Release Candidate for the… specifically for the stuff that we want to release candidate.
**Donal O'Sullivan** 10:56 Yeah.
**Braydon Kains (Google LLC)** 10:57 There might be some new ones that, Roger and I have been talking about.
adding, but I don't think we need to delay the release candidate for that. I don't think we want to… like, I don't think we would need to change anything that's…
**Donal O'Sullivan** 11:08 Let's do this.
**Braydon Kains (Google LLC)** 11:09 So we can go, I think.
**Donal O'Sullivan** 11:10 Yeah, okay, cool. Yeah, makes sense. I'll try and… yeah, I'll try and get that today, or probably tomorrow morning, I guess.
Yeah, and I'm also changing… I was looking at changing the filter package name, or just the… yeah, because I know there was an issue, an open issue about that, I don't know, did you hear the… Discussion we had earlier, but
**Braydon Kains (Google LLC)** 11:29 Oh, is this the, the one in, in CORE, or the.
**Donal O'Sullivan** 11:36 Yeah.
**Braydon Kains (Google LLC)** 11:36 by a filter with the different…
**Donal O'Sullivan** 11:39 Yeah.
**Braydon Kains (Google LLC)** 11:39 Patterns, yeah.
what were we gonna change the name to? I was actually going to use that package for something soon, so I don't know what.
**Donal O'Sullivan** 11:48 I don't mind, I was gonna just create a pull request, and then… I guess we could have a discussion there, or if you have ideas here. I was just gonna call it, like, String Match or something like that, because I know there was an issue saying that the package name is too generic, and it gave an example from the,
**Braydon Kains (Google LLC)** 12:05 Hmm.
**Donal O'Sullivan** 12:05 you know, from the Go, the Go dev site that is, like, it shouldn't be generic, should be specific, so… I guess it's not only for string matching, though, it could be any type, isn't it? So…
**Braydon Kains (Google LLC)** 12:16 Yeah, I mean, it's… Right now, it's mostly… it's being used for, like, matching names? Names of metrics and attributes, but also, like, names of… volumes, I think? In the… Remember, is it being used for that? Actually, I don't remember.
but, I mean, like, it is… It is for string matching, generally, so I think that's a fine name.
It feels… It feels a little bit like getting pedantic to…
**Donal O'Sullivan** 12:49 Yeah.
**Braydon Kains (Google LLC)** 12:50 That filter package is too generic, like… Come on, like, that's what it's doing, but whatever.
**Donal O'Sullivan** 12:56 Well, we can close the issue as well, I guess, if that's easier.
**Pablo Baeyens (Datadog)** 13:00 If it's what it takes to change the name, then I'm fine-tanging the name, but yeah. I also feel like it's not a very important issue to handle, but… I don't know if it's worth fighting over that.
**Donal O'Sullivan** 13:14 But can we just leave it then, and maybe close the issue? Like, is the person that opened the issue still active?
I know it's a parenting thing to…
**Braydon Kains (Google LLC)** 13:23 Where was…
**Donal O'Sullivan** 13:24 time on this work.
**Pablo Baeyens (Datadog)** 13:25 I don't remember who was it.
**Braydon Kains (Google LLC)** 13:28 I wanna check who… what is…
**Donal O'Sullivan** 13:30 I can say the name here, but I know it's recorded.
I'll put the issue in the chat, will I?
**Braydon Kains (Google LLC)** 13:39 Yeah, sure.
**Donal O'Sullivan** 13:40 If we can find it.
**Braydon Kains (Google LLC)** 13:45 Cause I have a… I have a guess.
**Donal O'Sullivan** 13:51 Your guess is probably right.
**Pablo Baeyens (Datadog)** 13:58 I mean, I'm fine if you just… ping the author, and if they don't reply in a reasonable amount of time, like, maybe ping them on Slack as well.
We disclose it, you know.
**Donal O'Sullivan** 14:13 Yeah.
I just put it in the shot there.
**Braydon Kains (Google LLC)** 14:19 Okay.
**Donal O'Sullivan** 14:21 The old one as well.
**Braydon Kains (Google LLC)** 14:22 This is from… yeah.
Two years ago, over 2 years ago.
**Donal O'Sullivan** 14:27 Yeah.
No, it was only because I know, Pablo, you put it in… we briefly mentioned it a couple weeks ago.
**Pablo Baeyens (Datadog)** 14:36 Yeah, I mean, I think we should do something about it, either close it or address it. I don't mind the name, but I don't think it's the end of the world if we change the name, I… That's what it takes.
So weird. But if you want to, like, reach out to the person on… Like… wife, that could be…
**Donal O'Sullivan** 15:01 Yeah.
Yeah, okay, cool, so I'll… yeah, I'll go… I'll go with that approach for now.
**Braydon Kains (Google LLC)** 15:06 The only point I can see to steelman this argument is that we have a filter processor, and so having a filter package in core might be a bit awkward, but also, I don't know if it's really worth getting.
up in arms about. String Match also sounds fine, as a name, I guess.
the…
**Donal O'Sullivan** 15:30 I don't mind, to be honest. I was just going, like, the Unix kind of name of, like, stir match or something like that.
**Braydon Kains (Google LLC)** 15:34 Yeah.
**Donal O'Sullivan** 15:35 mate, something stupid.
I don't… I don't really mind. I'm happy to reach out to him, and if he doesn't reply, I'll just close the issue as well, so… Whatever you guys think.
**Pablo Baeyens (Datadog)** 15:48 Yeah, do ping him on the issue on… if you want, on Slack, on…
**Donal O'Sullivan** 15:53 Okay. Yeah, sure.
**Pablo Baeyens (Datadog)** 15:54 Yeah, let's wait a bit on… yeah.
**Donal O'Sullivan** 15:57 Yep.
Thanks, guys.
**Pablo Baeyens (Datadog)** 16:39 For host metrics we want, we… Heart-ending dark, like… document or something on what semantic versions… what semantic dimensions we were going to use. I don't know if… We want to wait until we've done… dealt with the system namespace of metrics, or… or how do we want to do it?
**Braydon Kains (Google LLC)** 17:06 I think… well, I still want to write the document that explains that, like, we're going to stabilize and freeze the original schema.
**Pablo Baeyens (Datadog)** 17:13 And then… Hmm.
**Braydon Kains (Google LLC)** 17:15 new features will only be added through semantic conventions.
I just haven't…
**Pablo Baeyens (Datadog)** 17:22 Okay, right now.
**Braydon Kains (Google LLC)** 17:23 I just haven't written it yet.
I still need to. I keep on getting led around by the nose by random stuff the past few weeks.
**Pablo Baeyens (Datadog)** 17:33 Yep.
No worries.
I'm in.
I think everybody's getting… Tung around with security, at least, recently.
**Braydon Kains (Google LLC)** 17:44 Yeah, it's between, like, security and a big internal launch we have coming up, and trying to, like.
Fix random performance problems people are complaining to me about.
Stuff like that.
**Pablo Baeyens (Datadog)** 18:02 Okay, cool.
And… We heard from a couple weeks ago, the… Like, if we wanted to remove or change any configuration setting, I think you, Braydon, mentioned something about the options for silencing logs?
**Braydon Kains (Google LLC)** 18:28 Yeah, I'm trying… So, I've thought about this a little bit, where, like, what if we could Filter certain error logs by string, like, use the filter slash stir match whatever package, and be able to filter out strings that way directly at the logger, but the more I think about that, the more I think that's kind of brittle anyway, because the strings for errors could reasonably change.
And the filters might go away, so maybe having… Individual mutes and stuff is… the right… call, it just feels so lame. It has to have a switch for every possible error that can happen, and mute individually.
Seems kind of silly, but… can't think of a better way. The only better way is filtering, being able to filter logs, which is brittle.
So, I might just… Be okay with it and accept it.
**Pablo Baeyens (Datadog)** 19:32 Just these errors… Is it, like… Something produced by… go PSUDL, or is it something produced by the operating system, and it ends up being plumped?
**Braydon Kains (Google LLC)** 19:47 it's a mixture of produced by GoPS Util and produced by the Go Standard Library OS package that gets used by GoPS Util for things. Like, they will surface those errors as well.
Alright.
And so it's… because it's… not, like, error strings that we necessarily control. Like.
What we could do is have prefixes to these, like, put… wrap our own error around it.
And then…
**Pablo Baeyens (Datadog)** 20:20 Like…
**Braydon Kains (Google LLC)** 20:20 Say, we won't change the string, so you can filter based on this, but… But at the same time, a lot of people are using that mute all process errors flag that mutes everything.
And if we removed that and replaced it with filters, people would have to write a filter for, like, every single one, and that would be kind of awkward, too.
So, I wonder if… Maybe we can get around the awkwardness of that config by… Changing it to, like, just a substructure of, like.
Of mutes, where it's like a mute errors, and then there's a bunch of sub-options.
At least then the config will be… a little bit… cleaner?
Doesn't really solve the problem necessarily, it just might look nicer.
But it's also then breaking the hell out of the config before 1.0 just for, like, Slight config optics.
So, I'm… I'm thinking out loud. It's… I… I can't really… Can't really… I don't know if I can solve this before… before we want to cut 1.0, so…
**Pablo Baeyens (Datadog)** 21:36 I don't see a good way to solve this.
**Braydon Kains (Google LLC)** 21:39 Yeah.
Yeah, other than that, the only config thing I want to… get… get right before 1.0, because I… I guess this kind of counts, is the mDataGen feature that can… Like, metric… where the metrics builder config could be… could use that filter package to turn on and off metrics or resource attributes en masse.
I would like to try and get that in before 1.0, so… I should revive my filter package PRs that I sort of just, like, left hanging, because I stopped pinging about them.
But actually, in the collector, I have the PR limit, so I'm… I'm actually at the limit right now. I can't open anymore.
**Pablo Baeyens (Datadog)** 22:41 I mean, about, you can add exceptions for individual people. I don't want to make an exception just for one person, but if we put a process so that people can request exceptions, I'm happy to, like.
**Braydon Kains (Google LLC)** 22:54 I feel like that might be a good idea, just in general.
Because we get certain people complaining about the limit, but, like, we can't get rid of the limit, realistically.
so we could… we could make it like a… Kind of like how you, like, request membership.
**Pablo Baeyens (Datadog)** 23:10 From…
**Braydon Kains (Google LLC)** 23:11 for hotel, it's like, can someone on the maintainer or at least approver's team vouch that you're a real person who's not a bad actor opening PRs, you're just opening a lot because you're passionate, and then will accept the the… No.
**Pablo Baeyens (Datadog)** 23:28 Also.
I did change, I'm now noticing, the exemption rules, so that if you have an account that is old enough.
or you have merged enough VRs, then you won't have any.
Limit, so maybe…
**Braydon Kains (Google LLC)** 23:43 Oh, okay. Maybe I'll try. I haven't tried, I just know I have 3 open, and I haven't wanted to go through the rigmarole of, like, trying to open another, but I'll try it and see if I can get through anyway.
**Pablo Baeyens (Datadog)** 23:55 Yeah, okay, cool.
**Braydon Kains (Google LLC)** 24:03 So yeah, I'll prioritize that now, so we can unblock, like, the last sort of big config change to… To host metrics.
**Pablo Baeyens (Datadog)** 24:21 Cool.
Anything else we should discuss?
**Igor Peschinskii (Datadog, Inc)** 24:29 Yeah, I opened, post-AD default detection PR.
If anybody… Interested interviews.
**Braydon Kains (Google LLC)** 24:40 Yeah, I'd like to review it. I'll… I'll get to it today.
**Igor Peschinskii (Datadog, Inc)** 24:45 Thanks.
**Braydon Kains (Google LLC)** 24:45 Because we are… Going to be using this.
Using, like, basically what the recommendation from that issue is, what we're going to be using in something we're launching soon, where we want.
Host… host resource detection to work, like, exactly like… like semantic conventions, so… Yeah, I'll try and review this and help get it through, because it would be good.
**Igor Peschinskii (Datadog, Inc)** 25:08 Cool, thanks.
**Pablo Baeyens (Datadog)** 25:15 you know, all… Try and take a look.
Okay, and you did some tests on the… The startup time, and that seems fine.
**Igor Peschinskii (Datadog, Inc)** 25:33 Yeah, the start of time with clouds are fine, because… Detectors from other clouds are failing fast.
Burton.
Where Kubernetes, for example, it takes around 4 or 5 seconds, because of, I think, because of, EC2 detector.
Which… Just keep retrying, like, until the timeout reaches.
**Pablo Baeyens (Datadog)** 26:06 Okay.
And is that… I don't know if it's a good idea to produce a timeout or not.
But maybe it would be good if it is configurable.
But I don't know if… Whatever library we are using for this allows you to configure that timeout.
**Igor Peschinskii (Datadog, Inc)** 26:38 You actually can configure retries in the resource detection processor configs.
But I… I suggested in the PR that… If user wants to configure something in detectors or in the processor, then… It's probably better to not use default detector, but to use the recommended configuration, which is described in README.
**Pablo Baeyens (Datadog)** 27:08 Weird.
Okay, yep.
Cool.
We were discussing… something about the OPAM hosting detection, earlier today, well, ZADA appeared.
Bundy to look at me, and I think maybe it would make sense to eventually talk about adopting this algorithm there as well, but… Yeah, well, something for the future. I don't think… I think for this group, maybe we focus just on the resource detection processor, and then for other implementations.
Boop.
We'll figure it out. That's for.
Cool, I guess that's… It…
**Braydon Kains (Google LLC)** 28:29 I think so.
Thanks, everybody.
**Pablo Baeyens (Datadog)** 28:32 Yep.
To you.
