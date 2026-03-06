SIG: Python SIG
Date: 2026-03-05
Duration: 31 minutes
Zoom Recording URL: https://zoom.us/rec/share/bp2SfBH7-cmYZpUvnD6SDRLC4jwGXogSUbHDomXe9rR8ebI5YHPIWnFB3GSJBOkn.XINWW0C1XcFDYBfB
============================================================

## Zoom Recording Transcript

**Riccardo Magliocchetti** 00:35 Hello.
**Josh Winerman** 00:39 Hello, Ricardo.
**Riccardo Magliocchetti** 02:24 Welcome to this week's Python SQL.
We'll wait a few more minutes for more people to join. In the meantime, please add yourself as an attendee.
in the notes document, I'm sharing the chat, and also if you have
Any last, you know, topic you want to discuss?
Or… Feel free to add it to… They're not as well.
I'm just starting a thing now.
I mean, so…
Okay, I think we can start.
Welcome again.
Tammy, do you want to…
**Tammy Baylis** 04:17 Hi, Ricardo. Hi, everyone.
I… well, I think, the main thing is we renamed the board. Thanks, Mike, for suggesting that. It's now, Python PR Digest, and,
Yeah, I… I… there's still a lot of PRs. A lot did get merged for the release, thank you, Ricardo. There's several… several left, so have a… have a review… review. I don't have much to say today.
**Riccardo Magliocchetti** 04:53 Yeah, like, now that we have a release out, I think.
We can spend more time reviewing stuff.
Yeah.
**Mike Goldsmith** 05:02 Yeah, I think now we've got the still bot stuff there, that we will start to see stuff in here. We might be able to, use a filter or a group by on this to see what is still, because I don't think you see labels on this view very easily.
But yeah, a filter might help, like a still one versus a non-still one.
**Tammy Baylis** 05:26 Right, yeah, I've, seen stale, or PR's getting…
existing PR is getting marked as stale already, and I think in another week or two, those will be closed, so…
**Mike Goldsmith** 05:39 Yeah. Yeah.
**Tammy Baylis** 05:41 I'm excited.
**Mike Goldsmith** 05:43 Yeah, yeah, I'm looking forward to, like, the stuff. It was definitely a two-stage thing, where the marking still and then closing will be a little bit after.
**Riccardo Magliocchetti** 06:03 Okay, thank you both.
Any other comment?
**Mike Goldsmith** 06:09 What's something we did touch on, I think, a couple of weeks ago, I can't quite remember, is having some sort of, like, automated process to add issues and PRs to this board, so we don't have to do it manually. If that's something that we can… if we think is valuable, I can look at creating that, that GitHub action.
**Tammy Baylis** 06:28 I think that'd be fantastic, if you could please look into that.
**Mike Goldsmith** 06:33 Yeah, I've got… we've got some, I've done them before, where they can, they can automatically be run and added to a project board just like this, so it shouldn't be too difficult.
**Tammy Baylis** 06:42 Awesome, thank you.
**Riccardo Magliocchetti** 07:05 Thank you.
Okay, and we'll start with the topics, I think. Okay, the first one is from me.
Yeah, like yesterday, I released, 1.40.
A lot of stuff.
I think one of the, for me at least, interesting bits is that, we deprecated the longing handler in the SDK and moved
To the new location, in the log instrumentation.
And… went mostly smooth. The only issue… Was… Like, what…
some engineering instrumentation were not listed in the configuration file. We have,
In order to skip the releasing VAM and bumping a web version.
On our usual, risk process.
Luckily, I catch that at review time.
But I felt an issue, if anyone want to… Investigate?
But, like, I think this is something we can test.
And, yeah.
Doesn't make sense to go into details, but yeah, if anyone wants to…
to dig into a wireless process, I left an issue.
And, like, this is the first time it happened at, so… Not too urgent or anything.
Doodle thing, interesting.
Please rise, but, I don't know.
Why? But we got some issues with, Uv solving dependencies.
This is usually, like, something you get on your machine, never see this in CI.
But I think the…
This was fixed when I merged something in Contrib, and probably changed the ash, the repository, and…
unstuck, UV.
So, if anyone has any idea on how to avoid that… I haven't, but…
Feel free to dig also into the issue.
And… yeah, that's it for me. I think we can go to the other topics.
So the first one is from Josh.
**Josh Winerman** 09:58 Yeah, so, hey everyone, so this is sort of a follow-up into, something that was supposed to go to Core a while ago, but since Ricardo's, gone ahead and thankfully moved the logging handler into an instrumentation and contribib, it was a follow-up to a ticket in Core that I was wondering if it's still
valid, per se. So just adding an environment variable, to basically control the log handler config for auto-intermentation.
Simple as that. I was just… It seemed like this was discussed a while before I picked up the issue.
And… sorry, funny, Mike. And then, I was just wondering, I think there was an issue regarding agreement upon an environment variable name, especially with some overlap, with what exists in, the instrumentation nowadays, and…
I started opening up a work-in-progress PR to just see, where we might go ahead.
**Aaron Abbott** 11:01 Which… Which, config is the environment variable controlling?
**Josh Winerman** 11:07 I think it's the… we're looking at the, the hotel handler, so…
Not the root log bubble handler.
Because, it's…
Funny enough, I believe, the Python log level, or what is the variable called again? tell Python log level, controls the root level.
handler again, but I still don't think either or that applies to auto instrumentation at the moment.
I could be wrong, though, so feel free to correct me, Aaron.
**Aaron Abbott** 11:44 No, no, no, I mean, I think this…
it's a little bit subtle, so I'm trying to make sure I understand which problem we're solving, like,
there's… There's log level in hotel logs, but it's not…
I don't think there's any spec for, like, filtering. Somebody, you know, correct me if I'm wrong.
And then there's, like, the handler that we set up, which could have its own level.
But that's specific to, like, Python's logging module. It's not, like, inherently… Linked to hotel rate.
**Josh Winerman** 12:17 Sounds like that.
**Aaron Abbott** 12:18 More the water.
**Josh Winerman** 12:21 I would think it's more of the first, actually. But I… I could be wrong, I'm still…
Trying to understand the overall arcing of it myself, too.
**Aaron Abbott** 12:36 Okay.
Is, is there something in the spec about this? Just out of curiosity.
**Josh Winerman** 12:44 No, so I was following, like, I can link the previous PR, I think, too, that was linked to the issue in CORE, that was sort of talked about.
So there wasn't any agreement upon a particular… yeah, if you go down to,
Alright, I think it's 4203 is the one that's open in core.
Which has been open for a while.
And it had suggested using, there were multiple suggestions regarding an environment variable and which one to use.
for auto-information, but it seemed like the PR sort of went stale after a while.
**Aaron Abbott** 13:27 Yeah.
Yeah, I definitely… I'm having deja vu.
It's a bit, subtle and tricky, so… I think,
If we understand, kind of, like, what… what,
if we… I feel like if we understand what users want, and also what's, like, specific…
to OTEL, like, if there's something, I don't know, maybe we could look at Java or JS and see if there's other examples of what people have done. We can…
solve the problem, but it's just very difficult to communicate, because there's, like, 4 different logging things, you know.
**Josh Winerman** 14:10 No, understood, understood.
So is this kind of PR some… Because we've moved the handler into an instrumentation, is this kind of PR something we still want? Or,
Any thoughts?
**Aaron Abbott** 14:27 Yeah, Ricardo, any thoughts?
**Riccardo Magliocchetti** 14:29 you know, like, just, like, as I said in… to Josh on Slack, like,
like, I don't remember the issue at all, so I'll need to first understand the problem before, like, having an opinion on that.
But, like, as Mike said, Mike said, in the chat here.
I think, also Mike was working on something similar, like, probably, like, you, like, yours, like, on configuring, the stream handler.
Something like that, so maybe… You have a moment.
**Mike Goldsmith** 15:10 Yeah, that's right. I had a PR open, I think. We closed it because we knew we were moving it to the, contribo.
Yeah, I can't remember the details myself either. I would have to review what the cause was, but I remember…
I've got something to tell me that I think a user was telling me that they're having a problem with it, and then it was an old issue that wanted some… had gone a bit still. I came in, and then after creating the PR and not finding the existing one, then that's why we sort of had a bit of confusion.
Yeah, it'd be nice… I think it'd be nice to solve, but I don't… I've not looked at how it would be different to solve with what we were trying to do in the core repo versus the Contrib repo.
**Josh Winerman** 16:02 I think to try and address, I could be wrong here, so to try and address what Mike just mentioned, that hotel Python log level addresses the root level handler and isn't applicable for auto-instrumentation.
But I… this variable, presumably, would be applicable for auto-instrumentation to set up the hotel-level log handler.
**Mike Goldsmith** 16:25 Yeah.
Yeah, that sounds right.
**Josh Winerman** 16:31 Yeah, but… oh, thank you, Mike. But still, I was questioning if it's really needed at this point.
I can leave it to, to simmer at this point, too, if we wanted to shift away, but I just wanted to bring it up and see if we had any thoughts in the moment.
**Aaron Abbott** 16:49 Yep.
Do you think it could be solved in Contrib, now that the handler's been moved over there?
**Josh Winerman** 17:00 Yeah, I think it could.
**Aaron Abbott** 17:05 Yeah, I mean, I think we should… we should try to go that route then.
**Josh Winerman** 17:11 Okay, yeah, let me… I'll proceed, and then we can move on, and I can bring it up at a later date.
Thank you, though.
**Aaron Abbott** 17:19 No, no, thank you. I mean, we, part of the goal here was, like, to…
reduce the kind of friction, because we want the logs SDK and API to go stable, so if all these changes are sequestered to these unstable contribages, or…
intra packages that we can, like, do major version pumps for, then it's much easier to…
Make changes and try things out.
**Josh Winerman** 17:44 Okay, yeah, sounds good. We'll keep at it.
**Riccardo Magliocchetti** 17:50 Thank you.
Next topic from Surya.
on…
**Surya Teja** 18:05 Hey, hi. Yeah, so we had some discussion around two meetings ago, trying to see how we can reduce the load on, reviewers. So, we tried something with Skills.md and Copilot at work, where we were,
First, getting the, reviews by an agent, and then…
allowing reviewers to spend less time on it, so if anyone is interested, I can
raise a pull request with the MD file that we put forward, and
if we are getting free licenses from Microsoft for Copilot, we can use it and…
help reduce the load on reviewers. And coupled with this, we can also tweak our skills to first see the attributes, span attributes that are being added to new instrumentations are correctly aligning with the…
Hotel spec or not.
With this one.
**Aaron Abbott** 19:05 Do… do we have, like, a prototype or something?
**Surya Teja** 19:10 If the broader audience are interested, I can raise a draft PR or something with a prototype.
**Aaron Abbott** 19:18 Yeah, I know Lyudmila was working on doing this with Weaver.
So, would it use Weaver, or would it just be kind of like a… the L.
**Surya Teja** 19:28 Excellent.
**Aaron Abbott** 19:28 It does the check itself.
**Surya Teja** 19:30 the LLM is going to do the check. We are going to have a markdown file with a set of instructions that we wanted to follow. Say, if you want to review the hotel conventions, we are going to give the
location from which it can retrieve the attributes and check the code for seeing if it is, following the pattern or not. We will be dependent on Copilot, so what we can do is, we can do a GitHub Actions job.
With Copilot, summoning and, run this as a job, and you are going to get a set of, feedback review from the
Agent?
or the LLM, with the discrepancies of what can be changed.
It's similar to code review plugin, that we have in Cloud Code.
**Aaron Abbott** 20:28 I see. Would it be, like, integrated with the review feature in… that's already on GitHub with Copilot? Because I think we have that enabled already in OpenTelemetry.org. Or, like, you mentioned, Microsoft would give licenses. Would that be, like, we'd store some secrets in our GitHub, GitHub Action setup that would be used?
**Surya Teja** 20:47 Yeah, yeah, that's what I'm thinking. I haven't seen Copilot, inside, the OpenTelemetry repository, but that's how it works currently for us.
So…
I can work with someone from Microsoft and understand how it is being applied, and write some file… skills file, and…
Tested at.
See how it works.
**Aaron Abbott** 21:12 Okay. Yeah, because we, I think we chatted about this one, too. We could enable, I'm putting it in the notes, the,
GitHub Copilot Coding Agent, which I think you can also do similar things. I don't know how it, how it interacts with reviews, but I think
it wouldn't run in an action, and we wouldn't have to do any secrets or anything, but I'm the expert here, so just throwing stuff out there.
**Surya Teja** 21:37 Yeah, yeah. It's a similar idea, Aaron. So, the same thing.
**Aaron Abbott** 21:46 Yeah?
So… if you think it would work with the latter, that might be better, just because…
We don't have to do any kind of bespoke token stuff.
For secrets.
**Surya Teja** 22:02 Yeah, sure. Let me dig more deeper to see how the Copilot is being used in OpenTelemetry Org, so I have to understand a few things, because things will be different from what I have done.
previously. So, once I have a path forward, I can work on how we can integrate this as a GitHub Actions job.
And get reviews added to the PRs that are being raised.
**Aaron Abbott** 22:26 Okay, sounds good. And I think Trask is a… is aware of, like.
The rules, so to say, so if he,
has any ideas here, or you could chat with him, then I think whatever he says would probably be good.
**Surya Teja** 22:39 Yeah, true.
**Aaron Abbott** 22:42 Cool.
**Riccardo Magliocchetti** 22:53 Thanks.
Well, next topic is also from you, again.
**Surya Teja** 22:58 Yeah, it's, two pairs, that one is for adding sync instrument, Sync API instrumentation for open… sorry, Anthropic. It got all the approvals it needs.
To be merged.
And the other one is, response wrappers for… around OpenAI.
Espond's API?
Oh, did I paste only one link over there?
**Riccardo Magliocchetti** 23:42 No, no, the links were true, but one was wrong, so…
**Surya Teja** 23:53 One minute, my bad. I only posted one… Link.
There is one more PR from our topic.
**Riccardo Magliocchetti** 24:03 Ms. Wong. Aye.
**Surya Teja** 24:06 Yeah, 4155, yeah.
**Aaron Abbott** 24:22 I just resolved Dylan's comment on this one, and I was gonna merge it, but I don't know if you wanted to discuss it at all.
**Surya Teja** 24:31 No, no, I just brought it, Aaron. I did not want to bug you on the side, so just brought it up in the SICK.
**Aaron Abbott** 24:37 dear.
**Surya Teja** 24:37 Nothing.
**Aaron Abbott** 24:39 Yeah, yeah, no worries.
Dylan, did you have any,
thoughts on the should capture content on spans stuff in this one, or… I think… I think we did the rename, is that good enough?
**Madaket Beach (us-cam-5cc)** 24:53 Yeah, if we renamed it, that's good.
Yeah.
**Aaron Abbott** 24:58 Cool. I just, rebasted it, I'm just waiting for the checks to pass, and it'll merge.
**Surya Teja** 25:05 Thanks, Anne.
**Riccardo Magliocchetti** 25:25 This topic is from… Shuning?
**Shuning Chen** 25:31 Yeah, this is my PR for, creating embedding type and spam creation, so I have got, quite many comments, so I have dealt, deal with them, like.
Adding the missing response model name for the embedding span, and refactoring the…
start, stop, and fail API to make it general for Or, invocation types.
Yeah, so please, review again.
To see if, there are anything else to be modified.
**Riccardo Magliocchetti** 26:18 Thank you.
**Shuning Chen** 26:19 Thank you.
**Riccardo Magliocchetti** 26:25 But… This one from Kyiv.
**Keith Decker** 26:34 Well, yeah, just looking for more reviews on, enhancing tool call type. Aaron and Dylan, I went ahead and removed that INI.
Type from our, union.
just made it a generic type, and then I had to update Vertex AI's instrumentation to use the blob and URI types that we've added to Gen AI tools after, I think, they were originally added to…
to Vertex, so if you guys could look at that, that'd be… That'd be great.
**Aaron Abbott** 27:10 Alright, sounds good.
**Riccardo Magliocchetti** 27:18 Also, like, at last, if you have been made an approval for Contrib, So, fully, we have,
one more, like, green check, income to move this GenAir work faster, hopefully.
**Keith Decker** 27:37 Excited to be here.
**Riccardo Magliocchetti** 27:46 Alright.
And then… Peremanda?
From Lucas.
**Lukas** 27:55 Yeah, just reminders. We don't really need to go over these too much.
But, yeah.
This is the… header casing issue for Lambda, and then the other one is the… Protocy plugin.
For, generating the code for OTLP JSON.
I also… I've… I've separated… I rewrote the commit history, so it's 3 different commits, one for the plugin, one for the generated code, and then…
I think, one more for just updating the talks files and stuff.
**Aaron Abbott** 28:37 Yeah, I'm gonna take a look. Thanks for splitting that out.
I had one question on the, the CodeGen, it's like a separate package.
It's not gonna be published on PyPy, right?
**Lukas** 28:49 Right, yeah, it would just be internal.
**Aaron Abbott** 28:53 Okay.
I think, depending on how you generate it, there's, like, a…
way to do it, I think either you… I'm trying to remember.
But yeah, we should just make sure that it doesn't, that it's unpublishable. I think there's some special thing you can put in PyProject to…
**Lukas** 29:11 Okay, yeah, yeah, I'll take a look and make sure that… we… That that remains private.
**Aaron Abbott** 29:19 Oh, yeah.
Cool.
**Lukas** 29:26 Yeah, no rush on any of these, just wanted to make sure it was still on everyone's radar.
That's…
**Riccardo Magliocchetti** 29:38 Nope.
**Lukas** 29:38 That's all I have.
**Riccardo Magliocchetti** 29:40 Thanks.
Okay, so resources last… Topic for today… Anyone else?
I'll discuss something else…
Okay, I can add the last minute topic?
practice, right?
I've merged a long-running PR, I had opened.
That is, like, adding the… a basic HTTP-only OPMP client in Contrib.
So, yeah, like, I got a review from Pablo, thank you.
Yeah.
So now what you have… more interested in OPMP.
Since, like, this is, released independently, independently.
And what Billy's, like… Nearly, I think it's fine to have it emerged.
Okay, so if you don't have any more topics, you'll have 30 minutes back.
**Aaron Abbott** 31:11 Awesome.
**Riccardo Magliocchetti** 31:11 Thanks, everyone.
**Aaron Abbott** 31:13 Thank y'all. Later.
**Mike Goldsmith** 31:15 Thank you. Bye.
