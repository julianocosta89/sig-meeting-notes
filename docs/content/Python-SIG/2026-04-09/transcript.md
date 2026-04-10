SIG: Python SIG
Date: 2026-04-09
Duration: 61 minutes
Zoom Recording URL: https://zoom.us/rec/share/OhFHh8-P6yCLCKCMVNBLX4zbHIsGE97_5DYpo_jDAqb6Ql6K5dji44jcf3oU2oY9.sx4J35PLoqoedxzO
============================================================

## Zoom Recording Transcript

Riccardo Magliocchetti 00:02:02 Hello, everyone.
Mike Goldsmith 00:02:06 Hello!
Lukas 00:02:08 Nope.
Aaron Abbott 00:02:42 Hello, how's it going?
Riccardo Magliocchetti 00:03:19 Hello, everyone, to this week's Pytency call.
We're waiting a few more minutes for more people to join. In the meantime, please add yourself as an attendee to the notes.
And also, if you have any topic you want to discuss.
Well, as well.
And I'll share the link to the road signature.
Oh, so the agenda's packed, so I think we can start.
Welcome, everyone.
And let's start with the board triage. Pami, Wrote me that she is not feeling well.
And so, I'm doing that forever today.
Yeah, we have a bunch of old PRs, I think.
This is here, since a few.
or Swiss one?
You have a lot of new PRs.
Yeah, this one is interesting.
Yeah, anyone has something that we would like to highlight?
Like, really a lot of piers.
Mike Goldsmith 00:05:30 Yeah, we've had quite a few come in the last week or so.
Riccardo Magliocchetti 00:05:34 Yeah.
Anyway, like… This one, I already took a look earlier today.
And, like… strange PR, I think that… This user may be… A bot?
Because we also, like, opened another one, we're more or less the same… Issue, but… It's like we're adding a… Some more options to the Sphinx or to model for the matrix.
But at least, like, maybe it's me, but testing it does not change anything when… the docs is built, so I'm not sure if we're testing or… This is just, like, automation, I don't know.
And we're fixing, an old issue. What is market that's good first issue.
And I think that… with… like, this is, like, I have no proof, but… It looks to me that People that are using, automated stuff are looking for good first issue, labeled issues, so… And, like… I remember there was, like, an oldie show, I don't remember what it was about, but… when we have a label, we get, like, every week or so, a new PR for the same thing. I remove the label, and then we don't get the PRs anymore. So, not sure it's… You know, there's a cause effect, but… Seems strange.
Anyway… .
Aaron Abbott 00:07:26 Yeah, I think that's what it is.
Definitely heard about this from other people, too.
Riccardo Magliocchetti 00:07:35 So… But maybe we can stop.
Singap.
So… Yeah.
I see we have, like, a bunch of, Like, or, like, enable, lint rules.
For Ruff, and I think it's… Nice.
We merged some in core, and they asked a contributor to also do the same for Contrib, so they are on par.
I haven't found time to take a look.
I'll try to take a look more in depth in the next, dates.
Also, like, if you have time, feel free to take a look also.
This be awesome.
Mike Goldsmith 00:08:40 What do we typically do with, Dependabot?
PRs, do we sort of, like, group them together, or do we just try and work through them as we see them come up?
Riccardo Magliocchetti 00:08:50 I think it depends, because sometimes it bumps stuff that we want to be, like, on an older version.
Mike Goldsmith 00:09:00 Okay.
Riccardo Magliocchetti 00:09:02 Like, for example, no, this is DockerTest, should be fine to bump.
So… yeah, like, from a quick look, I think that… Most should be, like… Safe to merge, like… I think…
Mike Goldsmith 00:09:21 Do we have anywhere that we record which ones we have to keep to an old version for a reason?
Riccardo Magliocchetti 00:09:27 It's usually, like, in the test requirements, where we are testing multiple versions, so…
Mike Goldsmith 00:09:34 Thank you.
Aaron Abbott 00:09:39 Yeah, and I think, I think at some point, it was not possible to configure Dependabot how we wanted, or, I think at some point it didn't really support UV lock files well, also. I don't remember if that's been fixed yet.
Mike Goldsmith 00:09:54 Okay.
Riccardo Magliocchetti 00:10:02 Okay… So, I think we will move to the topics. Yes, we have a packet agenda.
We have some from me, after to be quick. I released, like, an hour ago, also, the new release.
No, release was not as smooth as… expected.
but at least, you know, we're… Stuff were easy to fix.
A trivial one was to list, But yeah, like, CI is a bit flaky today. When we have… Most Link are packages that don't use the stable version. We need to add them to… this group in the hdista.ini.
File?
I know, I noticed, I noticed that, that, the parallel release workflow will bump the releases.
And this one… got bumped from 0.63, or whatever, to 1.41, or 42, because of the PRO main.
And so, yeah, easy to fix, but if you don't know that, it's… Quandlest.
Like, you assume that the tool that bumps the version are aware of the version themselves, but they're not, and we're just, like, doing a replacement with… Be specialsh.
And then… Yeah, like, I forget to… when I… we moved to Ozgreen.
And now, like, in CI, we have a single… Job what, is green, only if all the other jobs are green as well.
I forgot that we had a different rule set for the… Release branches.
And so, yeah, like, an open APR on the Terraform files we use to update the settings there.
Like.
I don't know if it's the right solution, but I changed it to match what we have already, since it's working.
And so now, for having, APR mergeable in the release branch. We need all, Best to pass.
Which, like, has been the case recently, but, we can revise it later if… That's not the case anymore.
Aaron Abbott 00:12:44 Yeah.
I… Ricardo, I was just gonna say one thing, I think the admin repo is, like, bootstrapped from the existing permissions, but… Without, like, any regard to boilerplate.
So there's probably some cases… I mean, I think it's less important now that we're using this all-greens thing, but there's probably some cases where, You know, just refactoring stuff into, like, variables.
Or… and, like.
more extreme cases, I think you can do, like, 4H and Terraform and stuff like that. We could probably… Improve the situation a bit, but… Yeah.
Riccardo Magliocchetti 00:13:23 Yep.
And I don't know, the issue of fund, what… well… we had a job stack for more than 10 minutes, like, like, I canceled that after, like, a bunch of minutes, but… Didn't cancel fast enough.
Look at what we are using 30 minutes as a timeout for jobs. Maybe we can lower that a bit to 10 minutes, because, like, when jobs are stuck, like.
like, I'm not sure that the amount will kick… will kick in if the job is… stuck, as in, there were no output in the GitHub, interface?
But, yeah, anyway, like, I think most of our jobs are under 2, 3, 4 minutes, so it should be fine to use.
10. Like, not important.
And then the last one is that, I don't know.
where have this come from, since we haven't changed this code, as far as I remember.
But we started to get some failures, in CI, from PyPy on Windows regarding this test.
I don't have a version of PipePy new enough for my machine, but… I probably can use UV to set up it, but I don't have Windows.
So I'm not sure I can replicate.
But the idea, the idea, the problem is that, we expect that the last mock course as, Atai Matumili's, argument.
But that's not the case.
I think this is probably because we expect to get maybe just two calls, one without and one with the parameters.
And maybe we have a third one, or some… or more calls, anyway.
Lukas 00:15:23 I don't think this is unique to Windows. I actually saw this when I was running some local tests and assuming it was something with my machine, but yeah.
Just thought I'd throw it out there.
Riccardo Magliocchetti 00:15:36 So we get a volunteer for fixing that. Thanks.
Lukas 00:15:39 Sure, yeah, I can… I can try.
Riccardo Magliocchetti 00:15:42 Yeah, if you have time, please take a look.
Thank you.
Aaron Abbott 00:15:47 Yeah, and if we can make the test not sleep also, or sleep less time.
Riccardo Magliocchetti 00:15:58 Yep.
Aaron Abbott 00:16:00 Thanks, Lucas.
Riccardo Magliocchetti 00:16:02 This was for the release.
Next topic is, PR, but we have opened since a few.
But it's adding the… Exception parameter to the login meeting?
I took a look.
at last today, and I think we can simplify this a bit.
Because, like, Israel added, well, like, our logger emit, interface, like, we have multiple implementations, of the EMIT interface.
One is taking, like, the… A bunch of, arguments, and the other one is, taking a plane record.
And Israel also added a separated exception argument also to this version of the interface.
And since, you also added, The exception to the log record?
I don't think we need to also add the parameter here.
Because, like, I expect that people… We'll use… This other one version.
And doing that, we also simplify a bit the… What is, well, I left a review about the implementation.
Since I, like… We don't have to handle the case where the exception could be in two different places for the same call.
And so, yeah, if you have any opinion, please take a look. Like, the spec says that the implementation may have this other parameter.
So, I think that… Or maybe, no, no, maybe it's shield?
But… Yeah.
like… for the same reason, we have, like, the… just the log record, I think, at the exception.
Like, is it like any other, argument, right?
The logarithmic, function should take.
But, like, we can discuss that offline, like, And then, last one… no, not last one, but another one for me, like.
I opened up, Sketch PR for, Testing how we can integrate, or the OPMP client initialization in the… SDK configuration code.
I got some comments weeks ago that I missed, and so today I took a look.
And they're working a bit the… Initialization, like the error handling?
And I think… yeah.
Mike, correctly, like, since, like, I have a doubt on where to call the OPMP client?
because, like, in this PR, I'm calling it, before we set up the… the rest of the SDK, because I'm thinking of a use case where people want to get a remote config before starting the thing, because, like, maybe it's, Better to have, A proper configuration instead of having a working application.
But, like, for example, me, like, on my distro, I don't do that. I initialize the OPMP after the SDK has been configured.
And so, if you have any opinion on that… Please comment on the issue.
Also, I think I added some, yeah, notes there, but, like.
Maybe we can start with one entry point?
And… And if you have, you know, two different use cases, maybe we can add another one.
at the moment, the entry point has, underscore prefixed name, so it should be fine to change. Like, we are still experimenting with this PMP thing, so… Yeah, like, we can try and test different stuff.
So, if you have time.
and interest in the OpenP stuff, please take a look.
Last time for me, is time for real?
And… Yeah, like… looking at… This contribute PR.
the, the reporter was doing, like, a… A block list of some… What is the common?
A block list of some… I miss it as well? Nope.
Yeah, Michelle, a block list of some… Like, we were matching, some queries, and if the query matched.
They didn't create a spawn.
And so… like… they added that as a Boolean, which I don't think it's probably the best interface, so I… I see that there, that we can do… Implement the same in two different ways.
The first one is to keep the change local to this instrumentation, but… Just taking the queries you want to exclude instead of I'm adding a Boolean with a precise set of, or semantic.
So, like, Everyone that has maybe a different opinion on what to… skip, they can just host their own list of queries. And the other one is to maybe start using, like, at least start proposing to use the rule-based center.
And maybe people might want to drop some spans.
can write their own rules for the sample instead of adding, like, Instrumentation-specific changes.
I'm not sure we have, all the… pieces in order to do that easily with the current code in the rule-based sampler.
But, yeah, if the report has time, I'm willing to look at that.
I think… It would be… nice.
By the way, like, the rule-based sampling is an experimental sample that takes a list of predicates and… and outcomes?
And so, like, we can configure the sample, like, dynamically, and… And, yeah.
You can be a bit more creative with what you can draw.
Mike Goldsmith 00:23:18 Yeah, JavaScript does something similar when you're setting up these different instrumentation libraries, you can have… you can provide options in of, like, how verbose you want subspans to be, and you can opt in and opt out of certain things.
That might be something we can look at as a reference point to how they do that, and maybe similar… there might be other instrumentation libraries where we don't want to create child spans out of certain things.
Aaron Abbott 00:23:47 Yeah, is this… like, I know… for HTTP, we do the whole suppressed instrumentation thing, and I think the idea Is that it wouldn't work with a sampler, but the reason we do that is because there could be downstream spans, too, which you want to ignore, so I don't… I don't think a sampler would fix that necessarily.
Mike Goldsmith 00:24:13 Yeah, because, killing, or sorry, preventing certain spans from being created that then could potentially have child spans themselves, or break traces. It'll break trace graphs for a lot of the time, because the parent-child relationship would be broken.
Aaron Abbott 00:24:26 Yeah, I mean, potentially. I think… So I think if the goal is just to, like, filter out some verbose spans, but you want the rest of the trace, then it seems okay. But if the goal is, like.
like, the classic one we see is, like, oh, there's too many health check spans for, like, this HTTP server endpoint that I have, and, you know, something keeps calling the health check and it's spammy.
And so people want to cancel the entire… Like, all the styled spans of that.
And it seems like health check… was health check one of the use cases here, Ricardo?
Riccardo Magliocchetti 00:25:02 Yeah, I think this is just, like, the… Clean up a quid is wet.
Yeah.
So it's, like, probably a framework, or the… I think PG is doing under the hood.
Aaron Abbott 00:25:22 Okay.
Yeah, I mean, I don't have a super strong opinion on this one, just wanted to… share, like, the pro-con, I guess.
Riccardo Magliocchetti 00:25:32 Yep.
Yeah, I think we do… This is great.
Aaron Abbott 00:25:39 Go ahead, Ricardo, sorry.
Riccardo Magliocchetti 00:25:41 I don't know. Please go ahead. I was just saying that probably the sample is a bit too hardcore for this use case, since it probably will be, like, inside a trace what you care about.
Aaron Abbott 00:25:54 Yet.
Sounds good.
Lukas 00:25:58 Yeah, it might be… I know that the tracer configurator is pretty new, but it seems like that might be… You know, something that could be extended to Be able to, like, not create spans in certain contexts?
Not sure if I'm making any sense, but…
Riccardo Magliocchetti 00:26:24 Well, the tool required to update the specs.
So…
Lukas 00:26:29 Yeah, yeah, I'm not sure, like, where the spec's going there, but it seems like this would be, like, a natural… Future direction for Configurator, but…
Riccardo Magliocchetti 00:26:56 Okay.
And then… next topic?
From Mike, an update on the cloud config process?
Mike Goldsmith 00:27:07 Yeah, it's just a quick update on where we are with declarative Config. So I've been making good progress on this, thanks to Ricardo for helping out with reviews and getting things merged and stuff, so there's only a couple of things left.
In the list, which is the logger provider, which is ready for review, and then the service resource detector, which I know a couple of people have had some, queries on, I think I've answered those, so that's ready for review again.
Once those two things are available, then the last item is then making the public API, so actually being able to tie them in and actually reading a config when provided with using an environment variable. But yeah, I think we're close now, which is good to see. But yeah, just to let you know that this progress is We're closing in on being able to have a testable thing now, which is great to see.
Aaron Abbott 00:27:57 Yeah, that's awesome. Thank you so much for working on this, Mike.
What was… sorry if you already said it, but what was the status of, like, Of, like, kind of custom things or pluggable things that aren't part of the static schema.
Mike Goldsmith 00:28:14 In relation to, like, custom, like, propagators or things like that.
Yeah. Yeah, the, I can't remember which one it was. We talked about having an entry, like, a global entry point that then would look for particular patterns, and then be able to pull them in dynamically. I think we… there's an issue open to talk, like, to look for.
Like, having a generic path rather than just a static list, but that's an issue that we've got recorded.
I can't remember the exact details, but yeah, it's something that we are aware of, that there might be… Instead of having static lists of all of the things, it'd be good to have dynamic ones.
Aaron Abbott 00:28:57 Yeah, yeah.
I haven't dug into the spec or, like, looked really closely at what other languages do, but, you know, I imagine, like.
you know, like, there's, like, some GCP exporter or something like that, or some, whatever vendor exporter, or whatever, like… I don't know if it… is it… is it mentioned in the spec? Do you know, off the top of your head?
Mike Goldsmith 00:29:22 I can't remember off the top of my head, nor.
Aaron Abbott 00:29:25 Totally.
No worries.
Mike Goldsmith 00:29:26 Yeah, I'm not sure.
Aaron Abbott 00:29:29 Okay, yeah, that's okay, and I think it could always be, like, A follow-up thing, too, so…
Mike Goldsmith 00:29:34 Yeah. Yeah.
Aaron Abbott 00:29:36 Awesome, thanks again.
Riccardo Magliocchetti 00:29:41 Thanks, Mike, for updating the work.
Next topic is from Pablo, that we skipped the last week, and so… This time, we got it? Pablo?
pabcolli 00:29:53 Right, yeah, so, this is not my PR, but, this is a proposed small but breaking change to, How we handle log records.
So we had previously, well, currently, we have… we've got this special carve-out.
or record.msg, where record.msg, if you look at the Python docs, is supposed to be a string, but you can put an arbitrary object into that field, and it will get stringified.
So… it's… it's kind of like… It doesn't really conform to… the docs to, TreatRecord.msg as anything other than a format string.
And we went ahead and added this capability where if you do put a non-string in record.msg, then we end up Applying that to… body, and… exporting it.
As something other than a string.
And… I… so this, this PR, I think, you know, as we… as we kind of, like, move towards, log stability. I feel like this PR makes sense, but it's breaking, So, if we are gonna make this change, you know, now is the time to do it, I think.
Anyway, I wanted to get some opinions on this, if folks are interested. I will probably approve the change If anybody has any thoughts, then feel free to… Take a look.
Aaron Abbott 00:31:33 Okay. Thanks, Pablo. What's… what is the actual braking change? Just… I didn't quite get that.
pabcolli 00:31:40 Well, if you're currently, putting a non-string into… The format string field?
Then you're getting a, you're getting some sort of… What's exported is some sort of, struct. I don't recall what it is exactly.
You will be… so you would be, Using this… this special carve-out.
using… the format string in a way that sort of contravenes the way it's supposed to be used according to the docs, but it works!
So… Anyway, this is a… this is a simplification.
And it's in line with, sort of, the way Python is documented, so I figured this… this would be the time to make this change.
Aaron Abbott 00:32:34 Yeah, no, I agree, and I mean, I think also we moved this, the logging handler into this instrumentation so that we can you know, kind of, make breaking changes here, or stabilize this, or do major version bumps at a different pace than we do for the whole core, yeah. So I think this makes sense to me.
pabcolli 00:32:53 Cool.
Thank you.
Riccardo Magliocchetti 00:33:01 Thank you.
Like, I don't have a strong opinion on that.
But, like, I, probably, like, at the time we moved the code.
It will be probably there at the right time, but… You know, again, since now it's… outside the SDK, like, I think we have… The… our hands are a bit more free to… to change and introduce breaking changes, yeah, as Aaron said.
And… yep.
Thank you, Pablo.
Next topic is from Jayash.
Quest for review.
Are you here?
Yes?
Jayesh Hire 00:33:56 Yes, yes, Rippardo. So, during this, while adding this, this rule, there were many file changes, many files which I had formatted. So, I just wanted, like, like, the more eyes will be there on this PR, so, the lesser will be errors, so… yeah, that's it.
Some rules which were not typesafe, I have, ignored those rules.
So, if I, can give a summary of this rule, this rule just enforces that, if… if there is an import, which is used just for type annotation.
Then that import, should be inside a type-checking block.
So that, that import is not, imported delivering… During runtime.
Aaron Abbott 00:35:05 Could I ask a question? Like, I get the change. Was there specific performance issues you were facing, or, like, what was kind of the original reason to send this?
Jayesh Hire 00:35:18 Like… I didn't face any performance issue.
So, this rule was, listed on the original issue, and when I checked this rule, there were many, benefits of adding this rule. Like, if, the imports which are not necessary at runtime, if we just, skip those imports, skip importing those Python objects at runtime, then, It will just, reduce the memory use.
So… So I thought it would be useful to use this.
Aaron Abbott 00:35:56 Okay, yeah, I got you. I… I think it makes sense, Maybe this is one where, like, people might occasionally just disable it or something if it's, like.
annoying, but I think we could try it out, like.
I think in a lot of cases, what I've seen is Some of the things that are imported Might not be used, like, locally in the file, but they're definitely going to be in the import cache.
So if it's… I mean, like, I'm not sure… it probably wouldn't consume… extra memory in that case, like, maybe a single variable in the module, but… In terms of, like, side effects, if it's already been imported, I think.
But yeah, I mean, I think we can try this out. I was just curious where you were coming from.
Riccardo Magliocchetti 00:36:49 Thank you.
And we'll take a look.
I guess.
And, and thanks. Next topic, also a request for you for a PR from Shonig.
Shuning Chen 00:37:06 Yeah, so this is the PR for adding embedded metrics, so based on the last comment suggestion, I added the token metrics for embedding, span, similar to… O-O-M's bad.
I know this might be affected by the… A refactoring Pyreba.
Yeah, once that got merged, I will, yeah, I will make further modification, but the token metric change, can be reviewed now.
Liudmila Molkova 00:37:44 Yeah, Shireen, yeah, I'm sorry that my PR affects it a lot. My understanding that after the PR have yet merged.
this PR becomes much more trivial.
It's just a matter of returning, like, a few lines of code then.
I… I don't want to put more work on you, but I would rather… start with my PR, and your PR is still super useful in terms of tests.
It's just it becomes much easier.
And I'm sorry for further…
Shuning Chen 00:38:20 So anyways, yeah.
Keith Decker 00:38:28 Can we make sure we talk about that PR from Lumila today, too? Because it's blocking an agent and a tool.
well, I wouldn't say blocking, but it could vastly change those PRs as well.
Liudmila Molkova 00:38:40 Yeah, I have it in the agenda, I can put it to be the first of my topics.
Keith Decker 00:38:44 Okay, thank you.
Liudmila Molkova 00:38:46 Thank you.
Riccardo Magliocchetti 00:38:54 Alright… Mba… Lucas?
Lukas 00:39:01 Hi, everyone. Yeah, this, yeah, I just wanted either additional approvals or a maintainer to take a look.
Some, the last two have been sitting for quite a while, so I just… Didn't want them to get super stale.
So… and then, yeah, the top one is… This is the second-to-last package for getting the JSON exporter working.
So, yeah, there's two approvals, so, yeah, additional approvals are welcome, and then… I do have the follow-up for the actual exporter implementation as well.
Yeah, that's… that's all I wanted to add there.
Aaron Abbott 00:39:55 Awesome.
This one's maybe ready to merge, then?
Lukas 00:40:00 Yeah, there, yeah, additional reviews would be nice. There's, I think there's only, there's only two, but yeah, just wanted extra eyes on those.
But yeah, the last two are… should be ready to merge right away.
Aaron Abbott 00:40:16 Cool.
Lukas 00:40:16 Yeah, and then my last item is… Just wanted to discuss this briefly, so… while implementing the encoder logic for JSON, I think Pablo pointed out that there are certain instances where we, like, raise an exception while encoding.
When we encounter, like, unexpected data, like, like, maybe an invalid Any value or something?
I don't really see this as being a super big issue, because the SDK should really never create invalid data anyways, but, We… just to cover our bases, pablo recommended that… We should probably address this, so… the two options are… that I thought about is that we can either just, like, Kind of skip the field and log an error or a warning in code, and the export would still be seen as successful.
Or we would, raise the exception and just report, like, an export failure because of the invalid data.
So I just wanted to see if there's any additional thoughts. I think… Given that the data really… Yeah, I mean, there's advantages and disadvantages to each, but it's a pretty fringe edge case, so my feeling is that logging the error should be fine, so… I agree with Paolo here.
Liudmila Molkova 00:41:58 I made me some context, but hotel components should not.
Thrope.
Lukas 00:42:04 Yeah, so this isn't really spec compliant as is.
the existing proto-BOF encoder, it can technically throw an exception.
Liudmila Molkova 00:42:15 There's some hidden internal components can, but I think the assumption that exporter should never show.
Lukas 00:42:22 Right, I mean, as it is, all the exporters, from what I can tell, they don't catch that, they don't catch any encoding exceptions, so they would bubble up.
Liudmila Molkova 00:42:32 Yeah.
So, yeah, it's a fair idea that nothing throws but returns error gracefully, or we will have a catch-all. Well, not catch-all, but catch what we expect, right?
What we throw somewhere underneath and return the exporting failure to the processor.
Lukas 00:42:49 Yeah, so I was just more asking, do we want to just encode as much as we can in the encode function, and just kind of skip the bad data, or fill it with, like, null s or something? Or do we want to explicitly… we would still catch the exception, but we would return it as an export failure, and presumably everything would be dropped.
We won't even attempt to export it to the… to the backend.
Liudmila Molkova 00:43:12 I'd rather drop bad data.
So if we didn't validate it on the way in… And we didn't populate what's missing on this data.
Exporting some partial… Macy's tough is worse than.
Not exporting anything.
Lukas 00:43:33 That was kind of my thought as well, but the two scenarios where the exceptions are raised are pretty minor, but… yeah, we can, I don't know if there's any other… Yeah, I'm fine with also just, catching the… we can just catch the Update exporters to catch the exception and just return an export failure, if there's any encoding errors.
I guess the only downside is that this could clobber bad data with batching, but I… I guess… I think… Just doing this is probably a good first step for now.
Aaron Abbott 00:44:16 Don't… don't… doesn't the batch processor and, like, periodic thing, like, they would already catch the exception that comes out of the exporter, right?
Lukas 00:44:28 Oh, is that the case?
Aaron Abbott 00:44:33 I think so.
Should be.
Lukas 00:44:36 Oh, okay, and then I guess that maybe there's nothing to do here.
Liudmila Molkova 00:44:41 It maybe reduces the severity, but still… It implies that the batching exporter is used in front, and if people write the custom… sorry, batching processor, if people write custom processor, they would also need to encode this logic. So it's fairly low severity, but ideally, it's still good to fix exporter to 40 follow.
Spec guidelines of not throwing.
Aaron Abbott 00:45:08 Yeah.
I think one other thing, I don't remember if this spec does say this or not, sorry, I'll be brief here, The… it says that you can, like, return errors in a way that's, idiomatic to the language, I think.
Or, I might be thinking of a different part of the spec, right?
Liudmila Molkova 00:45:26 And I think the same one, and what you're probably alluding to, that exceptions in Python are a dramatic way to return an error rate.
Yeah.
Aaron Abbott 00:45:33 So we have, we have, like, this enum.
that we return right now with, like, the status being yes or no, and then there's, like, no information. So if you want to return a message, you have to, like, log it for, Just let the exception bubble up.
Liudmila Molkova 00:45:49 What did we do in other cases?
Aaron Abbott 00:45:53 Yeah, we can check, I guess, across languages.
Liudmila Molkova 00:45:57 I mean, other languages, let's just say, what did we do in Python? I think we don't… Thorough.
From the API, like, any public API, we don't throw, but internal SDK business, yeah, like, if it's common in Python to scroll between components, then… No, it's fine.
Aaron Abbott 00:46:17 Yeah.
Yeah, I would say so, but maybe it would be something we could look at for, like, a 2.0, but I think for now it makes sense to just be more defensive.
Lukas 00:46:32 Okay, thanks. Yeah, I don't… yeah, I… we can… we can, move on. I will, comment on the issue then, and then… Sounds like we actually probably just want to drop the batches, so…
Liudmila Molkova 00:46:49 Another point, sorry for, for, more context.
there are SDK self-house metrics, and I've seen some of them being added to Byton. We would probably report this as a metric, so we need some commonplace where it's caught.
And report it.
At least eventually.
Lukas 00:47:15 Got it, thanks.
Riccardo Magliocchetti 00:47:27 Thank you.
Lyudmila, you're next.
Liudmila Molkova 00:47:31 Awesome, let's talk GenAIO tools.
Okay, so… this PR… does a bunch of refactoring in APIs. It does not break any APIs that are used, currently for the future binary compatibility.
But it introduces a bunch of conflicts for the PRs against the tools that are already there.
So I think we should either… merge the existing PRs against the TILS, and let me deal with the conflicts and, incorporating new things into this, where let's merge this and make other people… Software, sorry. I… don't have a strong preference, but I still have a preference that I'd rather go with this, and not because it's mine, but because it has, A bunch of improvements that would make other PRs easier after.
Aaron Abbott 00:48:40 Yeah, I mean, that sounds good to me. Probably better sooner than later.
I guess, how much bigger would the PR be if, instead of doing it in, like, a deprecated step, and then sending follow-ups, we just did it all at once? Would it be, like, significantly larger?
Liudmila Molkova 00:48:58 I mean, this is… Not about breaking things, or… Like, for example, the… Can you open it, or… if we go to… or maybe I can present.
Aaron Abbott 00:49:13 Yeah.
Liudmila Molkova 00:49:15 Let me present, then… Okay, so let's say we go to embeddings.
This is unrelated.
How would we report token metrics for embeddings was just pure.
So… this, or… That's already actually implemented.
The invocation.
Support certain properties, certain methods, like get metric attributes, or get token count to report the token count.
I don't think this is wired yet.
So, like, the only change in the embedding metrics PR would be to call Something report metrics here.
Or report token metrics.
But let's compare.
So this is inference.
So it's backward compatibility crap.
So, we call… something here.
And in the same way as we call it for inference call, for LLM call.
We would do it for… the… Embedding call that we didn't do so far.
And the invocation on its own.
Has enough information to… For this metric recorder that we used before.
To record applicable metrics to this invocation, or the common metrics across all invocations.
I don't know, like, if we don't do this, then, the, the embedding PR would take its course, and I would… Need to update this quite a bit. To incorporate changes, and I don't know what does the abstraction model used there, how metric recorded has changed.
But essentially, this will be a bigger… Delta.
Not sure if it answers your question, sir, I'm sorry, I got carried away.
Aaron Abbott 00:51:40 No, no, I mean… I think my question was different, but that was useful. The embedding PR was you, right?
Shuning Chen 00:51:51 Yes.
Aaron Abbott 00:51:52 Yeah, I mean, what do you think?
Shuning Chen 00:51:57 So, for my… Metrics, that won't be a big change, I'm not sure, How the changer will be.
For Toko and the agent.
Eve, that would be a…
Keith Decker 00:52:16 For the… for the tool call PR, the… getting this… the Millows PR first would make my PR much more minor of a change.
It's just adding a few properties.
I know the tool call and the embedding PRs are both kind of reworking the metrics recorder to handle the additional invocations that are coming in, whereas Glute Miller's PR also Reworks that metric recorder to handle a bunch of different geni invocations, so they're all kind of going the same route, but just handling them a little bit differently.
Liudmila Molkova 00:52:59 Yeah, so this is the approach I used. I just generalized it, and now I use the prop… the methods on the invocation itself to report common stuff, the tokens and duration.
Keith Decker 00:53:10 Yeah, whereas the embeddings and the tool column PRs, also use GenAI invocation, but have now, switches inside that metrics recorder to… to generate the attributes it needs, versus this one that does it off the invocations themselves.
So I would prefer to go the invocation route.
Over the… the switch statements.
Riccardo Magliocchetti 00:53:42 So, Leah, you have your hands raised?
Surya Teja 00:53:48 Yeah, so hi, is this going to change the current code that we have in the instrumentation, like, OpenAI or Anthropic or other things?
I… sorry, I did not take a look around the XPR, so…
Liudmila Molkova 00:54:05 Yeah, totally fine. Yes and no. So the only changes here are… it was my intention to… disable, deprecation warnings. This guy is deprecated.
The methods on it are deprecated.
And I'm testing the old… libraries code with the new GenAIO tools to make sure we didn't break anything.
So, only changes are for the type checking.
Surya Teja 00:54:34 Okay, good. Thanks, Edna.
Liudmila Molkova 00:54:36 But eventually, like, I think I, Lucas brought it up, or somebody else brought it up.
that I should… Send the follow-up PRs to update its instrumentations to use.
New APIs?
It just can happen at our own pace. It's annoying as hell to edit everywhere, but this is a good forcing factor to update.
Aaron Abbott 00:55:02 Yeah, that'.
Surya Teja 00:55:02 Thanks, Litbra.
Aaron Abbott 00:55:03 Yeah, that was my original question, Lindmila, was like.
Liudmila Molkova 00:55:07 It's gorgeous.
Aaron Abbott 00:55:08 How much bigger would the PR be if we just fixed it all at once?
Liudmila Molkova 00:55:12 It's not… it would not be much bigger.
But I'd rather do it as a… follow-up, because I want this old versions of instrumentations that we sometimes release, sometimes not, to be binary compatible with this new gene articles.
And I want this PR to be the serving check that they are.
Aaron Abbott 00:55:36 Okay.
Yeah, I think… so, I think it was Marcelo. The comment was, like.
When you use the deprecated thing, it shows up in the type checker, but then I believe also when you call a method that's got the deprecated on it, it will emit, like, a warning to the console, so…
Liudmila Molkova 00:55:54 Oh, it will have, actually, the effect to the end users.
Aaron Abbott 00:55:59 I believe it emits a console message. Like, you can suppress it,
Liudmila Molkova 00:56:05 Hmm.
Aaron Abbott 00:56:05 But I think that was his only comment, was that it can be kind of annoying for users.
Liudmila Molkova 00:56:10 Okay, I thought that the users are the us in the libraries.
Aaron Abbott 00:56:15 Yeah.
Okay. Maybe, let me double-check that I'm not making stuff up, or somebody can keep me honest here.
Mike Goldsmith 00:56:24 Yeah, I read the same as well, I think, The… it… he was worried that a warning would be sent to library users, not just library instrument… library developers.
Aaron Abbott 00:56:40 Yeah, yeah, warnings can be admitted at runtime.
It's… It's a little weird, but… Yeah, I think you can suppress it, and you might be able to… no, you can't suppress it at the place where you decorate it, necessarily, unless we wrapped it with another decorator, but, there is, like, a suppression mechanism in Python, so I think it's a valid comment, but other than that, I'm okay to do it in multiple PRs.
Liudmila Molkova 00:57:09 So what we can do, I can unsuppre- oh, sorry, undeprecate this whole thing.
Switch libraries.
Like, wait, under prickie doll thing.
Leave just a to-do comment to update.
Or just update.
Then it will now have no effect on the end users, but at least we know we didn't break anything.
Lukas 00:57:37 I think you can use category equals none, but I'm not sure if that's Python 3.9 or 3.10.
that's just… I'm just reading the docs quick, so there might be another way to keep the… keep the… type checkers.
Aaron Abbott 00:57:52 Yeah.
Lukas 00:57:53 Inline, but not log.
Aaron Abbott 00:57:57 Yeah, that sounds like a good option, too.
Lukas 00:58:08 Yeah, the only thing to check would be the Python 3.9 compatibility.
Liudmila Molkova 00:58:15 Also, it exists since Python's rename.
Lukas 00:58:19 No, I'm not sure. It might…
Liudmila Molkova 00:58:21 Okay.
Lukas 00:58:22 Recent versions.
Liudmila Molkova 00:58:24 Okay, let me check this. I'll do it today, and if, if… If I can find a better way, I'll let you know. Otherwise, I'll just undeprecate LLM on vacation for now.
Aaron Abbott 00:58:37 Okay.
Liudmila Molkova 00:58:38 Cool, thank you.
And since I have 2 minutes of your time.
Let's try to pick the idiomatic way to… For a new pattern we'd like to introduce for the GenAI libraries to avoid the package squatting problem that we have.
And, I don't know, should I post it in the Python channel and we can vote on this?
Or should we just say, okay, But our option is.
Mike Goldsmith 00:59:11 Is there a reason why we wouldn't want to do this?
Aaron Abbott 00:59:18 Like, like, assuming we choose one of them?
Yeah, so, I mean, I think… there's, like, so I know of at least one that's… I think we have two of them that are actually already OpenTelemetry instrumentation, whatever, so there's Google Gen AI, and I think one of the Anthropic ones is like that, so… we already have those package names, but for pretty much anything else that we want to add, it's already been reserved, so that's kind of the context here. I think the risk is confusion.
like… Maybe we would rename OpenTelemetry Instrumentation Google Gen AI to Match this pattern just to make the confusion less.
But other than that, I think, Yeah, do you have any thoughts, Mike? Downsides?
Mike Goldsmith 01:00:12 No, I was just thinking… Yeah, I didn't think that we've already had some instrumentation libraries outside there. The confusion part is that we'd have some on the old pattern and some on the new, and would we want to migrate to the new, or would we just want, like, V2s or whatever, or, accept that there's some older ones that are on a different name? I'm not sure.
Aaron Abbott 01:00:31 Yeah.
Maybe let's put it in chat, and Beside there, does it sound good?
Liudmila Molkova 01:00:42 Awesome.
Thank you.
Aaron Abbott 01:00:47 Alright, thanks everyone, sorry we didn't get through everything.
Thanks, everyone's…
Mike Goldsmith 01:00:53 Bye.
Riccardo Magliocchetti 01:00:54 Thanks, everyone. Bye-bye.
Keith Decker 01:00:56 Thank you.
Erdenesaikhan Tserendavga 01:00:57 Thank you.
Lukas 01:00:58 Thanks.
