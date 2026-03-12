SIG: OpenTelemetry C/C++ SIG
Date: 2026-01-12
Duration: 24 minutes
============================================================

## Zoom Recording Transcript

**malff** 00:54 Hi, Tom.
**Tom Tan** 00:57 Hi, Mark. Good evening.
**malff** 01:01 Good evening. Can you hear me okay?
**Tom Tan** 01:06 Yeah, I can hear you.
**malff** 01:07 Very close.
Hi, son. Hi, Ali.
**Ehsan** 01:57 Hi, everyone.
**Tom Tan** 01:59 I guess so.
I don't know.
**Ali Sedighi** 02:02 Everyone.
**malff** 02:09 Tom, do you know if Lalit is joining today?
**Tom Tan** 02:13 He is not in office, so probably I assume he will not.
**malff** 02:18 Okay.
Oh, looks like, eSign may have some connection, issues.
Okay, well, I guess we can start, and maybe Lalit and Doug will join.
First of all, Happy New Year, everyone.
I know that this is… open telemetry has been very quiet during the winter.
We are back to… having regular meetings again. So, I hope all of you enjoyed the time off and vacations.
I don't have a lot of things to discuss, I only took a few notes in the agenda to Just to mention things I noticed in the upstream repo.
Inspect some antique commercials, and so on.
Everyone, do you have anything you want to discuss in particular? And Ali, do you have any questions you want to discuss as well?
**Ali Sedighi** 04:20 Honestly, I mean, technically, it is my first time that I've participated in the meeting.
**malff** 04:26 Okay. I don't think so, no, for now.
**Ali Sedighi** 04:29 I just want to figure out, the good, yeah, item to contribute.
**malff** 04:35 Okay. So, typically what we do during this meeting is, we get in touch to see where we are in terms of issues and PRs.
And when there are some technical discussion on things, it's a moment to exchange a bit.
Otherwise, for… More in-depth details, we tend to comment on the issue, itself, Like, for code reviews or debugging things, so this is just a time to catch up and synchronize.
But yes, feel free to ask questions if you have any.
**Ali Sedighi** 05:12 Good, thanks for your information.
**malff** 05:19 Okay, so, just to get up to speed.
On the spec side, a couple of things have changed recently.
The first thing is that the Jaeger propagator is deprecated in the spec.
We are not affected because CPP did not implement that anyway, but at least it used to be a mandatory item that we were missing.
And now it is an optional item, so I guess on that we are compliant now.
And, so since it's, it's deprecated from the spec, there is no point in trying to implement it.
And, so this is one… one less thing's, one less item to think about.
Also, on deprecation, the zipkin exporter itself has been deprecated as well.
So… My understanding that the ration for it is that Zipkin, either already does or will soon, accept the OTLP protocol directly, the same way Jaeger does, so there's no point in keep sending, in the Zipkin format to the Zipkin exporter, so that Zipkin… the exporter itself, the Zipkin exporter is deprecated.
But it does not mean that Zipkin is going away. We still can talk to Zipkin, however, that will be using OTLP later.
I… I haven't checked into spec.
Whether there are some dates there for the deprecation.
So… up for discussion, but I think the Zipkin exporter can stay in the codebase for now.
And by the time it is finally removed from the spec, then we will remove the exporter itself.
The other possibility is to move it to CPP Contrib, but it's more work.
And there are other things that need to be… to move to contribute before that, so I guess Zipkin can stay in the CPP codebase.
To discuss, of course.
And, another thing that changed recently in the specs, earlier, the spec was, improved to have some concepts of a logger configuration for tracer, meter, and logger.
And that configuration object, had some properties. One of them was to enable or disable the tracer, and the… the property name for that has changed. It used to be a disabled property, now it's an enabled property, so this is a breaking change in the spec, which is okay, because that part is still experimental.
So it has been renamed in the spec, and it has also been renamed in the file configuration in YAML.
And the next step is for CPP to align on that, so just… just change that Boolean.
Change the name and reverse value, and also we need to… Just, just so that we align on respect to avoid, To avoid confusion, I guess.
So, we need to… to have a small PR in the CPP area to adjust for that.
Any questions or comments on the spec so far?
Or things you have noticed that I missed?
**Tom Tan** 09:03 No, I'm outside.
**malff** 09:05 Okay.
Still on the… still on upstream?
Cementing Convention is doing a release. They have a PR open right now, so I'm guessing that the… The next release for Symantec Convention will come anytime soon.
Like, typically, if not today, in a day or two.
So, as usual, I will prepare, Code generation, again, for the semantic conventions to keep them up to date, in, in OpenTime and 3 CPP.
So, expect to see OPR soon, with, very good adjustment, as usual.
And still upstream, the file configuration project is getting closer and closer to a 1.0 release, and doing some last-minute cleanup.
So, it's currently at the risk candidate number 3, and the… the YAML schema is being cleaned up for things that are deprecated and should be removed, things like that, or some minor renaming.
So, I will probably have to adjust the config.yaml implementation in CPP.
Just want to info that as well.
So, I've started to do that last week already. There were some changes to remove the Zipkin, exporter supporting YAML entirely, because it was removed from the spec.
And also, there was some renaming done on the TLS area for the OTLP exporter and the… I mean, OTLP HTTP and OTLP gRPC exporter.
So, those are done, there are some other minor things to check. So, we'll probably have a couple of PRs as well for that.
So, apart from that, I have not, well, I have not been following closely all the swim repos, but this is just things I noticed that affect us one way or another.
So it's, otherwise, it's pretty quiet. We don't have a lot of work, induced by upstream changes.
On things to discuss before the vacation, Doug created, adjusted… Duke improves CI to report a lot of ceiling tidy, issues.
So, we have a lot of them, we just need to take some time to actually clean that up in general, so that we… We have… those needs to be cleaned up, not only in the SDK implementation, but some of them also are affecting the API itself.
Mostly some warnings about, missing constructor structures, things like that, just to be totally clean on the C++ side. Those should not affect the BI, but if we… when fixing that, we need to be careful about the changes.
To make sure we don't break anything.
So, there are quite a… I don't remember the number, but there are quite a few warnings to clean up, so it will take some time.
As usual, with what we have done with, CPP check earlier, and we've included what we use as well. The goal is to just Fix a few things, reduce the number of acceptable warnings that we can have, and continue to fix them.
So that ultimately, we… We clean all the backlog.
So expect to see a couple of PRs as well on that.
I did not mention that, but the last release was in, late November, I think?
And December has been very quiet, so I don't think we need a new release soon.
Because it's only early January.
But, Tom and Nissan, and you… Do you know if people need all of these just to… To be up-to-date with the code what we have, or if we can wait, like.
Maybe end of January or mid-February to do a new release.
**Tom Tan** 13:44 No requests from… from my side, I think.
End of this month for new releases, huh?
**Ehsan** 13:52 Yeah, January sounds good, end of January.
**malff** 13:56 I took, look, we have quite a few PRs, Yeah, 42 commits, but a lot of them are just bumping version numbers of this and that in CI, so it's, We don't have a lot of changes.
But I guess we can… yeah, end of January, or sometime in February, if we… we can probably make a new release just to… To stay fresh, I guess.
Okay before we go into the issues and PRs, I don't have a… Overgeneral things, If you have anything, you know… It's a… no, it's a good name now to discuss it.
Otherwise, we can go into the new issues.
So, things have been… Pretty quiet during the, during the winter break.
We don't have… A lot of new things.
This is basically a question someone, who wants to contribute some good, and he was looking at a small area to look at.
So, basically contributing a unit test to cover some behavior to make it explicit.
I think it's, it's okay. I mean, the area in question, which is to test this new variable, it's, It's not something which is, risky, I guess, but it's, it's always good to have more unit tests, just for coverage, and especially for code coverage long-term.
So, if he wants to contribute in this area, this is fine with me, but would be a good opportunity to have a small PR done in a small part.
To get up to speed with, contributing in general.
So, if it looks okay with you, I will just reply that, yes, a PR in this area is welcome, and we can have one.
It would be a low risk anyway, because it should be touching only the tests and not the code.
And not the production code, I mean.
So yes, we can accept that.
Yeah, sounds good. Sounds good, okay.
This one is for a moment. I did not quite get what he is after, exactly.
So, he found that, basically compiling PortoBuff with one C++ standard, and Appsell with another one.
or hotel CPP with another one just creates linking issues in general.
Especially on the Port of Betharia, and… So, this is most likely correct. The question is, What we do about it, and whether this is supported or not.
Oh, because this, I mean… This seems to be caused by protobuf itself, so, of course, when compiling a binary, it's better if you use the same C++ standard all over the place.
Oh… In his case, if there is a mix, it creates an issue.
The part I don't understand is that he has a PR for that, and I don't quite… I'm not quite sure what he intends to fix with the PR.
If it's too… a new… add new CI test case to make sure this thing works or doesn't?
And do you have time to look in depth on that?
It's, because it's not touching the CPP code itself, it's touching CI, and the way it is that… well, all the makefiles and the way it is tested in CI.
So… To me, it raised the question, whether this thing To mix and match whether we really intend to support it or not.
**Ehsan** 19:23 I think we shouldn't go in this direction.
**malff** 19:28 You know, my concern is that if we do that.
Then we basically commit ourselves to make that work, no matter what.
And especially, it might be tricky to support it, too, once… There are more changes in portal, but that makes that impossible, so…
**Ehsan** 19:50 Yeah, this is not the best practice to mixed versions.
**malff** 19:53 Yes.
**Tom Tan** 19:54 If we allow this, I think in future, there may be more ask, like a new version, different version, right?
**malff** 20:01 Yes.
Yeah, so the funny thing is, we… it's only make file already, or MakeFile or install, but there is no… There is no code change in the CPP code itself to make that happen.
So I guess, yeah, I'll ask Owen to clarify what his intent is to… We've had UCI.
But it proves to me that we should not… We should not… Add complexity like that and try to push report this.
**Tom Tan** 20:38 set the vocal…
**malff** 20:51 Oh, and my browser is acting up, suddenly I'm stuck.
Interesting.
I may need to… stop sharing and try again, or maybe, Tom Oresan, if you want to… To take it from now, and… And share your screen if you can, because mine is stuck now.
Okay, well, otherwise, I'll just go from memory. So… We have, Going from memory, if we have some other questions, like someone wants to contribute in a couple of places, I can reply to that.
On the PRs, most of them are very old.
Tom, there is a PR related to a change for, I think it was propagation of something.
**Tom Tan** 22:21 Yeah. Which is a…
**malff** 22:22 Yeah, and I only have one comment fair.
**Tom Tan** 22:25 Okay, let me resolve your comment, yeah.
**malff** 22:28 Okay, it was… yeah, from memory, it was just to test about the… some… some character, some space allowed or not allowed, something like that, so it should be trivial to resolve.
And then we can have Vaude Pierre, merged.
Okay. And… Sorry about my screen freeze, still going from memory. Other PRs, so there's the PR for moment, already don't make files.
For… for this issue with, portal, and, But otherwise, everything else is pretty old, so nothing really recent happened during the winter break there.
Any issues you, That you know of, or peers that you know of that you want to discuss as well?
**Tom Tan** 23:41 No from my side.
**Ehsan** 23:42 Nothing from my side.
**malff** 23:44 Okay.
Okay, well, I think we can just close the call then, because it will take some… too much time to just shut down and start the call again to continue, and… And it looks like we are, pretty much covered already, so… Again, for… thanks for, everyone to join, and most importantly, Happy New Year again for… to everyone.
For me, it was a good thing to have some break, and To spend some time off, so… I hope, everyone, had some good time as well.
**Ehsan** 24:27 Thank you.
**Tom Tan** 24:28 Sure, great to hear that.
**malff** 24:31 Yeah, thanks, everyone.
But…
**Tom Tan** 24:34 Thank you, bye.
