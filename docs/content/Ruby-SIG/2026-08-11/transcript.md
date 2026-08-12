SIG: Ruby SIG
Date: 2026-08-11
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Matthew Wear** 02:09 Hey, how's it going?
Yeah, I think this is probably gonna be it for today. I saw that, Hannah and Kayla are not gonna make it.
**Xuan** 03:36 Aye. Yes.
**Matthew Wear** 03:40 So… Yeah, I guess we can take a quick look at things.
So, yeah, let's just take a quick look at, the spec SIG, I guess.
And… yeah, two… two somewhat interesting and relevant things, I think, for us, and that is that, Trask is putting together this… Semantic Conventions Conformance Repo.
And… I need to look more at this repo, but basically, let's take care of someone.
Oof.
I'll show you the output first, and then maybe we can look at the repo, but… He's basically kind of setting up these, These small test apps that exercise all these, instrumentation libraries, and all these different languages, and, I think it ultimately pipes this all to Weaver to kind of check that the semantic conventions are… that are emitted are what are expected.
Oh.
So… So ultimately, yeah, I think that's a pretty interesting project, and we should… see what he's doing for Ruby, and then we should see what we're actually emitting for Ruby, and kind of create some issues to bring our… instrumentation up-to-date with semantic conventions.
And… and that's probably a can of worms. I don't really even know where we are in terms of semantic conventions. I kind of know… A while ago, there was, like, this scheme to, like, have Kind of a configuration option to, like.
emit kind of the, you know, the classic semantic conventions, and then turn it on to kind of emit the newer ones. I'm… I know some SIGs kind of went through that process already, like, JavaScript already kind of removed, like, the compatibility, option.
But I have a feeling that we're probably a little bit behind that.
Do you know?
**Xuan** 06:23 Yeah, yeah, those are, like, old, dupe, new, I think.
**Matthew Wear** 06:29 Yeah.
**Xuan** 06:30 That, yeah, it was kind of, yeah.
**Matthew Wear** 06:33 Are we still, kind of, We still have support for those, old dupe and new, or,
**Xuan** 06:40 As far as I know that this exists. I think the plan was that to remove them after 6 months, but I'm not sure how that goes.
So…
**Matthew Wear** 06:54 Cool, yeah.
Yeah, I guess we'll talk about that maybe next week when more people are around, figure out where we are on that timeline, but… Oh.
But yeah, this is kind of the output, and that's gonna be wrong.
**Xuan** 07:11 just for this one, so they use programmatically, to determine if the spec, if the semantic commission is up-to-date, is that right? They don't use, like, some AI to, like.
to do this, right? Because… Program to do… to… to do the check.
**Matthew Wear** 07:36 Yeah, it… He said he set up some small test programs, So… I have yet to figure out where they all exist in… in the repo, so, there's a chance that, I think, like, this… This repository's, like, brand new.
As of last week, so I know Trask has been working on this kind of separately, so it could be that all the tests maybe are not ported over just yet, because that…
**Xuan** 08:07 Oh, okay.
**Matthew Wear** 08:09 This thing I'm showing you, it's on, like, Trask's GitHub.
So,
**Xuan** 08:14 Okay.
**Matthew Wear** 08:16 So yeah, like, I… I still need to figure out where the actual tests live, but, But yeah, he introduced us at the specs thing, and that was the question that I asked, and he said, these are actual programs that are running to exercise the instrumentation, and that's what it's kind of based on.
**Xuan** 08:38 Okay.
Makes sense.
**Matthew Wear** 08:42 So, there's that. And then, There's packaging, Which is kind of… yeah, there's a packaging SIG, and they have a, a first release, and right now, it works for, like, Java.net, Python, and Node. And basically, this is kind of, like, similar to the operator instrumentation, but it's kind of for Linux hosts, and if you just apt… app, or you'll install OpenTelemetry, then it will, It will basically, Patch all of your running applications, to… to use OpenTelemetry?
there's a blog post about it, they were talking about Ruby, that… Yeah.
For Ruby to be added to it, we need the auto instrumentation gem released, and then the second thing that we need is declarative config.
So, I know both of those are in progress, but… There is work now in the, no.
the injector, like, the Ruby… like, there's Ruby support for the OpenTelemetry injector, which is kind of, like, half of what needs to be there for the packaging SIG, but then there's actually the packaging part of the packaging SIG that is kind of waiting, I guess, on the… Ruby Instrumentation gem to be released, and us have declarative config support.
**Xuan** 10:28 For the, for the injector, I don't know about this stuff, but it, it, just a quick question. What is the mechanism, like, behind those injectors?
**Matthew Wear** 10:43 The mechanism behind it is…
**Xuan** 10:45 Yeah.
**Matthew Wear** 10:46 It's basically a shared library.
**Xuan** 10:50 Yeah, okay.
**Matthew Wear** 10:51 And… it will set some environment variables, I guess, like, when you… Okay.
when you, like, I guess execute, like, the Ruby command, it'll execute, like, ruby-R or something to, like,
**Xuan** 11:12 Okay, I see.
Okay.
**Matthew Wear** 11:15 Oh, go ahead.
**Xuan** 11:17 I saw it's something like, you know, the… the goal? They have, like, injected something into the, like, kernel to do the, all the tracing stuff. I saw it's the same thing, but… I guess it's not…
**Matthew Wear** 11:32 Yeah, I think it's a different mechanism that Go is using. Okay.
But… But yeah, I guess there's… there's a blog post, I don't know.
what all this says, but oh, yeah, I guess it kind of gives you the, the overall, Summary… Boom.
Yeah, so… I think, mainly, that is… Those were the relevant parts of… the spec SIG… actually, also probably somewhat… Related, although this conversation got, like… It got kind of cut short because Josh, who brought it up, had to, like, leave midway through, but… They're talking about handling a invalid UTF.
Boom.
policy, and I know that, like.
I think Bart had a, a PR for a very similar issue.
But…
**Xuan** 12:52 Yeah, yeah, yeah.
Also, comment on that. So, I think other language, they have, enforced UTA, UTL, not UTL.
UTF-8, well, I guess… well, from, from the AI told me, I think Ruby is a special case that, doesn't enforce this UTF-8, so that's why he had an issue, and that's why he added the PR to enforce UTF-8.
**Matthew Wear** 13:24 AI said that we were kind of the odd… odd SIG out on that.
Yeah, that's… that's super surprising.
No.
But yeah, there is some… I guess some issues where they're… Talking about how to actually handle this.
And I think the… from what I was gathering from it, it's like, basically, if anything reaches an exporter and it's not UTFA, it's kind of, like, considered a bug on, like, the… Either the instrumentation or API side.
But… I think Bart was handling this at the exporter level, just because it's… it's hard to track this stuff down, I guess, further upstream, and that's kind of, like, one, you know.
One kind of, like, call site where you could handle all this stuff.
**Xuan** 14:28 And then, from the other language, maybe my memory fitted, but, I think for other language.
if… if the character is not UTF, UTF-8, which means we'll have encoding issue, and they… I think the JavaScript and Python, At least one of them, they will just ignore this malformat.
A string. The entire, span.
So they don't, they don't really have a, Catch… exception for those, kind of, issues.
But that's what I, at least what I remember from last time I checked out there.
implementation.
August.
**Matthew Wear** 15:13 Alright, yeah, that's all useful.
Yeah, so that was basically the spec SIG, I just kind of added this note that…
**Xuan** 15:28 Hmm.
**Matthew Wear** 15:29 Packaging is blocked on declarative config, and Ruby instrumentation release.
**Xuan** 15:36 Yeah, I, I made a revision on, on all the comments about, to separate those, to separate those, functions, so I have that ready, so you can take a look. But I haven't, changed the name yet, I'll do it after to change from hotel or config to maybe config, yeah.
**Matthew Wear** 16:00 Cool, awesome. Yeah, I'll take another look at that today. Appreciate you addressing that so quickly.
**Xuan** 16:06 Yeah, and also, I also have some comments about the email variables.
Yeah, basically, if you open up here, you see what I said about the… Well, what I'm thinking is, you know, variable… so, at least for Go, I think it makes sure that it doesn't… So, so the SDK has the amount variable… the SDK respect to those immun variable.
I think COVID… what COVID does is, if your user chose the, you know, choose the decorate configurations.
the GoDecular configuration, make sure… It will never reach to… to, so basically, it would create everything for a user.
So… so it will never reach to those, those, you know, variables, in those SDK. Yeah. And also, there's a migration, YAM file.
That is, but if a peer user wants… still want to use this, you know, variables, they can do it, but I think in the future, they will not allow this.
**Matthew Wear** 17:26 Yeah, I feel like that's just, like, a whole other can of worms that we will address at some other point in time, but yeah, my understanding is that it's kind of… Like, like this shows right here, that the environment variable should be… Should be, kind of, applied At this level, not kind of at the component level, that there should be, like, environment variable substitution that happens into kind of the… the YAML file before we process it, is that right?
**Xuan** 18:00 Yeah, yeah, yeah.
**Matthew Wear** 18:01 But the components themselves should not, you know, should not be.
**Xuan** 18:07 Yes, that's it.
**Matthew Wear** 18:08 environment.
**Xuan** 18:09 Yeah.
**Matthew Wear** 18:09 environment variables,
**Xuan** 18:11 Yeah, basically we try to create everything for user. Like, not we, I've been asked the deco computer to create everything for user.
Oh.
Fair.
**Matthew Wear** 18:25 Yeah, so I feel like that's gonna be a lot of work, and it's probably gonna, like… I don't know, it's probably gonna be a little disruptive, because I think a lot of people are using those environment variables today.
probably Shopify comes to mind.
Boom.
But the spec is the spec on this stuff, so I think we're gonna have to make that migration one way or another once we, figure everything out.
So…
**Xuan** 18:49 Okay, yeah.
**Matthew Wear** 18:50 So yeah, I… I haven't thought too much about that work, but probably… what I would imagine happening is that we would add, like, this, Environment variable substitution to our declarative config once we have it done.
And then, once we have that That setup, then we'd probably… Go through the process of removing the ones, that we… Currently have in our codebase, so that there's kind of, like, a… You know, an upgrade path of some kind.
**Xuan** 19:26 Yeah.
**Matthew Wear** 19:30 And then, yeah, like, I had the same concern that you have for custom components. I was kind of saying that in my comment, that… You know, that we'll have this startup initialization, load order, issue, probably, and, I'm not saying that we shouldn't do it, but we shouldn't do it for, like, our initial version, you know what I'm saying? Like, later on down the line, once we get things working, we can talk about how we want to handle those, and see if there's a reasonable way to do it, but I feel like it's… it's like an additive thing, we don't need to We don't need to worry about it right now.
**Xuan** 20:10 Okay.
**Matthew Wear** 20:21 So, James put this… Pose.
Not here for Contrib. Anything else you want to talk about in Core while… While I was there.
**Xuan** 20:30 No, no, yeah, just as I was saying.
**Matthew Wear** 20:33 Cool.
Alright, so James points out Or he's asking what we should be testing in appraisals, and he kind of points out, like, at least 3 different ways we're doing things there, and I don't know if there's enough people to actually make a decision on this, Today, so I'll probably just note that we should discuss this next week.
But… But I think what he found is that The min-supported, plus the latest, plus some… Manually added in the middle.
And then some tests, like, every min and major is supported.
And some tests, kind of like the VIN of each major, and then the major.
Correct.
Min of each major, and then the max of each major. So, 2227, 2034… I think I'll just make a note, Oh.
**Xuan** 21:39 Why? Do you know why you want to make the change? Is that because of current, current, option is not, is not working?
**Matthew Wear** 21:51 I don't know.
Maybe we can ask.
What is our question?
**Xuan** 23:04 Why… why we needed to change the options, right?
Or have, yeah, have different options.
**Matthew Wear** 23:37 Alright, we'll just note that for now, I think.
Do you have any opinions on this, or… I haven't really thought about it.
**Xuan** 23:57 Are you tied up.
Yeah, because I think… If it's working, or it doesn't give any, Yeah, and why do I change it? Okay, well, we can just wait for, for his response, that's the motivation is, yeah.
**Matthew Wear** 24:15 Yeah, I suspect the inconsistency is not great. We should probably have, like, a, an approach and stick to it that much I'm on board for… on board with, but… I haven't thought too much about, like, which approach is… is the best.
And, Yeah, I would be in support of us making it uniform, if there's something that we can agree upon.
But at the same time, yeah, it is… If it isn't broken, then why fix it, is the other, The other way to think about this…
**Xuan** 24:57 Or he wants to improve it, like I said, to make it even more consistent, then if that's the case, then sure, we should do it.
**Matthew Wear** 25:07 Yeah.
Anything that you wanted to talk about in court, or contrib?
**Xuan** 25:23 Yeah, to have one PR that, may need a, it's very easy, just, the agent marked down.
Pretty straightforward. There's many of the… And I looked to make sure the… the LLM, instruction error.
Best?
**Matthew Wear** 25:44 Cool, yeah. I will take a look at this.
This is the one, right?
**Xuan** 25:49 Yeah, it's the same as the one I have on the… Occur.
**Matthew Wear** 26:18 Right, yeah, I will take a look at that, add it to the agenda, so that other people can take a look.
And then, yeah, I just put these bullet points about the off.
semantic conventions conformance that we looked at earlier.
And then, yeah, auto instrumentation, we're still… Is our release kind of still held up on some, like, credentials or something being set up properly on the repo? Is that…
**Xuan** 26:48 I don't know, I've asked Tina about this, I haven't tried to release… After the… after last time, it failed, so… I don't know what happened to the roof, to be honest, yeah.
**Matthew Wear** 27:06 Okay, cool, yeah, I guess we can talk about it next time. And then, yeah, like, if… If you ever want to look at the… Price point installer, that's… that's up there still, too.
**Xuan** 27:17 Yeah, yeah, yeah, yeah, definitely.
**Matthew Wear** 27:23 Cool, I guess I will put our names.
as attendees.
And that's all I have. Anything else that you wanted to talk about?
**Xuan** 27:36 No, that's everything I have in my mind, yeah.
**Matthew Wear** 27:39 Cool. Yeah, so I'll take another look at the declarative config work. I think that's coming together pretty well for at least our V1.
And then I'll also take a look at that, agent markdown, or intrim.
**Xuan** 27:54 Okay, thank you.
**Matthew Wear** 27:56 Yeah, no problem. Probably see you next week.
**Xuan** 28:00 Yep, yep, thank you, see ya.
**Matthew Wear** 28:02 See ya.
