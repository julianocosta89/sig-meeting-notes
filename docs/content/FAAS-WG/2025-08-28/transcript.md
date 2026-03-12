SIG: FAAS WG
Date: 2025-08-28
Duration: 33 minutes
Zoom Recording URL: https://zoom.us/rec/share/SsQ7P3yq4yfGhZQqlIOiCq6b4kAJVdNY065lVXyBA5fX01dEb1loDjgdiWI8pFRR.jXPneJpD5qbg4QLL
============================================================

## Zoom Recording Transcript

**Tyler Benson** 02:00 Hello, hello, everyone!
**Warre Pessers** 02:04 Hello?
**Serkan Özal** 02:05 Lowe.
**Tyler Benson** 02:19 Everyone ha- having a good week?
Jorge, you have a good vacation?
**Warre Pessers** 02:24 Yeah, I did, thanks. I'm a little bit ill now, getting back, but … My week's been good so far.
**Tyler Benson** 02:33 Okay.
**Serkan Özal** 02:34 Okay?
**Tyler Benson** 02:37 Where'd you go on your trip?
**Warre Pessers** 02:39 I went to Italy, used to go there when we were children, and now went back for the first time, so it was a very nice, … Experience being back, after such a long time.
**Tyler Benson** 02:53 Nice.
I haven't been. I want to go sometime, though.
**Warre Pessers** 02:57 Yeah, you definitely should. If you need any, recommendations, you can always hit me up.
**Tyler Benson** 03:05 For sure.
What part of Italy?
Rome?
**Warre Pessers** 03:09 Yeah, this time we went to the… to the north, to, Lake Garda, I don't know if you know it.
**Tyler Benson** 03:15 No.
**Warre Pessers** 03:16 But… back in the day, we used to go to, like, Tuscany, I think is the English, ….
**Tyler Benson** 03:24 Yeah.
**Warre Pessers** 03:24 translation, and also to Umbria, … Yeah.
**Tyler Benson** 03:28 Okay.
Sounds fun.
Yeah, definitely. I assume you had some really good food, too.
**Warre Pessers** 03:34 Yeah, definitely, definitely.
**Tyler Benson** 03:46 Hi, James. Welcome.
**James Thompson** 03:51 Hey.
**Tyler Benson** 03:58 Shall we go ahead and get started?
**Serkan Özal** 04:00 Yeah, I think so.
Maximit said he will be joining, but maybe we can join later, but not sure about Ivan, so I believe we can start.
And, yeah, first of all, congratulations to Gory as, for his promotion to the maintainer status.
And he has been a very active member of, FAS Group.
And, especially, we put great effort for the Lambda context propagation issue, which is, I mean, very complex and includes multiple things to work in place together to be able to properly propagate the context.
Yeah, I mean… good job, Vari, and congratulations again.
**Warre Pessers** 04:51 Yeah, thank you so much. It really does mean a lot to me to get the trust from both of you existing maintainers. So I'll try to live up to the expectations.
**Serkan Özal** 05:07 Yeah, thank you.
**Tyler Benson** 05:09 We'll have to have you, learn how to do releases next time.
**Warre Pessers** 05:13 Yeah, yeah.
**Serkan Özal** 05:21 Okay, … Any specific topic from you guys to discuss?
Maybe, James, from you?
**James Thompson** 05:32 Yeah, so from my side.
there's two issues. The first one is about the SEMCO of PRs, about improving the definition of the attributes.
Right? And supporting the… the entity.
Right, for a FAS instance.
Alright, so I've put that in the agenda.
**Serkan Özal** 05:55 Okay, did you send that PR to the GS or GS Country Preparatory?
**James Thompson** 06:02 I've posted it in the Slack channel, yes?
Alright, but it's a SimConf issue.
Right, full phase.
**Serkan Özal** 06:15 Okay, okay, I got it, okay.
**James Thompson** 06:20 Right.
**Serkan Özal** 06:23 Okay, we'll be looking into that, but… I think it will require… approval, from the… from the group, who is responsible for the semantic conventions, but as a first group, I think we can review and give our approval, if that's okay. Thanks for reminding us, yeah.
**James Thompson** 06:45 Yeah, yeah, because usually the Simcoev want a subject matter to review it.
**Serkan Özal** 06:51 And before that, they will prove it.
**James Thompson** 06:53 Is that true?
Yeah.
**Tyler Benson** 06:56 Do you want to just walk us through it right now? If you want, you can share your screen and kind of just give us a quick summary.
**James Thompson** 07:03 I'm on my phone, because the time of day it is for me, alright, because it's 1AM.
**Tyler Benson** 07:07 Yeah, well….
**James Thompson** 07:08 Thanks, thanks for staying up with us.
Yeah, right, but effectively, what it is, is first off, 1PR introduces a standalone ID for the F-Z instance?
Right?
So, let me just quickly… … Yeah, so there's now an explicit ID for the FAS.
Right, so that way… We can create an… reusable ID… Pull the ins… pull the… In… yeah, for it.
Okay? And currently, we're using the cloud resource ID.
But when you are using it on-prem, provider.
the cloud resource ID doesn't really fit.
And at the same time, it's a… supported property in Elastic.
Okay.
Alright, so it's just adding one additional attribute.
**Tyler Benson** 08:03 So, is it, is it removing the FAST instance ID?
**James Thompson** 08:09 No, so… So, I just… sorry, I got a bit confused there. So, there's adding an explicit ID for the FAS, right? So it's faz.id.
Alright.
Because currently we have cloud.resource.id.
But if you're not using a cloud provider, it doesn't… you don't really have an ID.
**Tyler Benson** 08:31 Okay?
**James Thompson** 08:33 Okay.
So that's one.
And the other one is… renaming the faz.instance to faz.instance.id, so that you could have a faz. instance entity. I've put… the links are in the agenda.
Right.
Yeah, so that way you can have the… a reusable entity describing the FAS instance.
Right. Yeah.
**Tyler Benson** 09:08 Okay.
… Just out of curiosity, what's your motivation for this change?
**James Thompson** 09:17 Right? So, I come from where we run a lot of stuff on-premise, so we started off by looking at it Right? How can I capture the on-prem?
Right? Because we're not using… we don't use the commercial cloud providers.
So, that's where they started looking at the… how can I provide an ID?
for the function where I'm not using a cloud provider.
**Tyler Benson** 09:41 Okay.
**James Thompson** 09:41 Okay, alright, and then when I've been looking at the entities, right, we're trying to describe having a look at this instance of the FAS, right, what's happening with it?
We couldn't actually capture It's not actually defined an entity for that.
Yeah.
**Tyler Benson** 10:01 Okay.
So I think a lot of this makes, makes sense to me.
the concern I have is around implementation, actually. So, like, the things that you're trying to ask for an ad, are they generally available in these other places?
**James Thompson** 10:26 Alright, yeah, alright. Yeah, so… One of them was just a rename of an attribute, right, just so that you could create an entity, right? So that's one of them, so there's no issue with accessing it.
**Tyler Benson** 10:39 Right.
**James Thompson** 10:41 Okay? And the other one was… rather than using cloud.resource.id, it's using faz.id.
**Tyler Benson** 10:50 Okay?
**James Thompson** 10:52 Right, so… It's… there's no issues with accessing the information. It should all be readily available based on… it's not… Needing additional information from the platforms.
**Tyler Benson** 11:04 Okay, so I guess the next question is, it comes around to implementation of, of this in the libraries, right? So, once this gets, approved or, you know, merged or whatever, Who's gonna go through into the various implementations and actually make the change?
**James Thompson** 11:25 Yeah, so, like… I'm more than happy to do the .NET ones, etc, because that's my background.
**Tyler Benson** 11:33 So I don't think we have a whole lot of .NET instrumentation, to be honest.
**James Thompson** 11:39 there is a Lamba, right? There's Azure Cloud Functions, contribute projects, etc.
Alright.
**Tyler Benson** 11:52 We don't publish a specific layer for it, though. These are just libraries that you add in as a dependency, right?
**James Thompson** 12:01 Cheers.
**Tyler Benson** 12:02 Okay.
Got it.
So, but then for the primary, languages that we support, you know, Python, JavaScript, and Java… even Ruby, I don't think that we have anyone that, would… would… necessarily work on that right away, right? Do you… do you have anyone that, … Can help, or are you just familiar with the, … with .NET.
**James Thompson** 12:41 No, like, I've done Java… you know, I can do Java, etc, alright?
Right.
**Tyler Benson** 12:48 Okay.
Okay.
Serkin, worried? Any… any questions for him? Any feedback?
**Serkan Özal** 12:59 Nope, I just, I mean, I was just, circling down the PRN as far as I see.
Actually, there are some… I think the… the major, change, the… actually, the new introduce, attribute is the fast.function.id, am I correct?
**James Thompson** 13:18 Yep.
**Serkan Özal** 13:19 Okay, … there are some… some other changes, but I think they're just… I mean… cleaning, I'm refactoring, I'm just cleaning… cleaning up and updating the things, maybe?
Right?
**James Thompson** 13:34 some… Yeah, like, the PRs are very deliberately very small, very focused, like, a lot of it's just… The… the way in which the documentation is generated.
**Serkan Özal** 13:50 Okay. So you also added the documentation for other attributes, too, as far as I see.
Right?
**James Thompson** 14:00 What do you mean?
**Serkan Özal** 14:02 Actually, I mean, I have seen, for example, you… you edit descriptions for the… fast invoked name, invoke provider, and the other attributes, and as far as I see, there… there was no description for those properties, so I think in addition to the new attribute, you also added some….
**James Thompson** 14:22 Some description and enhancement of the… of the explanations of the false attributes.
**Serkan Özal** 14:29 Right?
**James Thompson** 14:29 No.
**Warre Pessers** 14:30 I think this may be due to how GitHub displays the diff. It looks a little bit weird indeed.
**James Thompson** 14:39 Yeah, alright.
what you'll probably find is it's… the ID numbers for the notes change, so it shows it as added.
Right.
So what you're better off looking at is the changes to the model. So I only made changes to the YAML files.
**Tyler Benson** 15:02 So I think what he's saying is we should focus on the YAML files, not the Markdown files.
**James Thompson** 15:08 Correct.
**Tyler Benson** 15:09 It's a man involved.
Our automatic user modified.
**Serkan Özal** 15:15 Okay, so markdown files are automatically generated, right? Okay.
**James Thompson** 15:18 Cheers.
**Serkan Özal** 15:19 Okay.
**James Thompson** 15:21 Yeah, so that shows the limited scope of these changes.
**Serkan Özal** 15:31 Okay.
Okay, we'll look into that after the… after the meeting, sometime this… this evening or tomorrow.
**Warre Pessers** 15:44 Yeah, same for me. I can help out on the JavaScript implementation, because I know that they do something with a deprecated semantic convention attribute for the FASID currently, so I would need to look into why… That is still the case, but then I think we can change to your new ones as soon as the package is available, the new version.
**Tyler Benson** 16:13 Another thing, to point out is I think a lot of these semantic conventions are likely… somewhat benign in terms of mainly just informational. I would… I wouldn't be surprised if there's, no vendor, whether metric, tracing or whatever, that Actually depend on the keys of these attributes specifically.
Does anyone know if that's not the case?
Like, is it gonna make any functional impact to any various, OpenTelemetry, depending vendor, like, Datadog, New Relic, Dynatrace, whatever, if these change?
**James Thompson** 17:04 Yeah, like, they should not make it… my understanding is they should not make a difference to them, right? Because, A, these aren't stable attributes, right, so they're expected to be changed, right? But… As far as the backends are concerned, is… The instrumentation are emitting a collection of attributes.
Alright.
**Tyler Benson** 17:27 Right, no, sometimes there are specific attributes that back-end vendors will look for and modify their behavior accordingly. I don't… I think we're both in agreement that that's not the case with these specific attributes.
**James Thompson** 17:42 Yeah.
**Tyler Benson** 17:44 Correct?
**James Thompson** 17:45 Yep.
**Tyler Benson** 17:46 Okay.
Got it.
I… I commend you for going through the effort to do this. … I… It's a little, surprising, though. It would be easy, in my opinion, for you to just not do this, and carry on, like, the existing way, or use one of the existing attributes, or even just keep it custom, and don't worry about it. I don't know.
But anyway, bravo to you, keep up… I mean, we're happy to have you, keep, participating in the SIG here, too.
We need a .NET expert.
Anything else you wanted to talk about?
**James Thompson** 18:46 That's alright.
**Tyler Benson** 18:48 I know this is late for you, so thanks for joining, but … That's right. Yeah, we'll look into that.
**Serkan Özal** 18:54 Yep, thank you.
And… Any other topic, guys, discuss, other than the context propagation?
Work from worry.
**Warre Pessers** 19:06 There was….
**Tyler Benson** 19:08 New, new, layer releases out this, this past week.
**Serkan Özal** 19:15 Yeah, there was, some, some weird GitHub issues, we just… Didn't trigger the… the release?
actions, workflows, on the tag push, and then, Tyler just deleted and repushed the tags, and then the flow triggered and released the new versions of the layers.
I didn't have a chance to, to try the newer version.
But we'll be looking into that sometime this week, mostly tomorrow, Friday.
At least for the Node.js and the Java layers.
And I would have my setup for those.
To… to test the simple cases.
**Tyler Benson** 20:06 Sounds good to me.
**Serkan Özal** 20:11 Yep.
For the, the context propagation, improvements, by worry, as far as I see worry from your message, when you try with New Relic, and they just didn't support To see the whole trace through the spell links, right?
**Warre Pessers** 20:32 Yeah, they just don't show span links in any way whatsoever, … I also tried with Datadog, but it wasn't that obvious to me how you actually use Datadog with OpenTelemetry Collector. They kept trying to push me in the direction of some sort of Datadog agent, and then I, left it because I, was leaving on vacation, but I may look at that again, or maybe some other, vendors as well.
**Tyler Benson** 21:04 I would be surprised if Datadog supports span links, to be honest. I don't know that they do.
**Warre Pessers** 21:11 Okay.
**Serkan Özal** 21:13 Yeah.
**Tyler Benson** 21:14 I could be wrong, though.
I used to work there, and, you know, way back when they certainly didn't, but maybe they've added support for it since then?
**Warre Pessers** 21:26 Yeah, I… I can double-check, but… That seems, … very probable that they don't, as, like, New Relic, for example, didn't support it at all either.
Yeah, actually….
**Serkan Özal** 21:43 Yeah, that was… that was my worry, too, because… I mean, the span linking, is a kind of new things, and then… which is not… I mean… I mean, actually, not many folks aware of these… the spell linking things, and also, proper implementation of the spell linking in the backend, in the observable backends, tracing backends.
It's complex and, I mean, harder than the other parts. So, for New Relic and the other things like Datadog, other companies, vendors like Datadoc, and the, maybe the Dynatrace and the others.
to me, it is not surprising to not… to see that they are not supporting the CPAN links.
So, that was the reason that why I just asked Wuri if he has time to try with the, I mean, big vendors, big tracing vendors. Therefore, actually, I have been thinking of… whether for the process spans, the SQS process spans, as… they are pointing to the produce recipients, their produce recipients, through the link, CPN link, and… instead of the CPAN link, to the… to their producers, What if we have… What if it points their produce recipients as the parent contacts instead of the link?
So… so in this case, since they will be, related to each other, I mean, the producer's depends and the process recipients through the regular, parent-child relationships, they will be able to, show in the, I mean, almost all the… by all the vendors.
But use the spell linking for… pointing I mean, lambda invocation span points to the producer's span with the span link, and also SQS process spans points to lambda invocation span with the span link, again, but the SQS process spans will point to their producer's pants as the parent, so no spelling kick needed.
Actually, I was thinking about this approach.
Because in this approach, … I believe that the process depends and the producer's sequence will be able to show in the same trace, same view, same UI, for almost all the tracing backends, tracing products.
So it may have, I mean, less impact on the existing functionality for… for the community, so that's just, I mean, my… my idea.
**Tyler Benson** 24:35 So, I… I… I've been involved in conversations around this a lot in the past, and it's always been a debate.
I… I think that, there is merit in having, … Lambdas prefer the parent-child relationship over span link, but… that span linking is defined, I think, in the specifications, so if we wanted to change that, I think that the best option would be to make it a configuration.
So that, users could choose, to prefer, having the remote be the parent instead of span-linked.
**Warre Pessers** 25:22 Yeah, I can agree with that, because indeed, as Tyler says, the way that the span linking is being done at the moment, that is something that is actually in the semantic conventions.
So… I don't know if we should, by default, switch to the… parent context stuff, it does make sense to me to also support it, because then, we are supporting way more observability vendors, But then I think maybe the approach Tyler suggests makes more sense to me.
**Serkan Özal** 26:01 Yeah, to me, having a configuration, I mean, I am fine with having the… having such configuration to switch between the spam link and the… and the regular parent-chat relation. … I'm just, I mean, trying to say that, by default, I think we should prefer The parent-child for the process expense to their producer spends.
Because, I mean, by default, still users will be able to see The things, end-to-end in the same… same page for… for the majority, maybe all of the, all of the vendors.
And even with the parent-child relation, still, there are big improvements in this… in this approach, in this PR, because before this PR, we was… we were just, we were not able to… trace each processing span individually, because there might be multiple producer spans, and… We… we only have the single invocation span, and then, since we are not able to… I mean, points to multiple parent spans at the same time, that was failing, but in this approach, still, there will be direct relation between the process spans of the HSQS messages to their own producer's pants.
So that is, I mean, technically and semantically feasible. And also, there will be links to the invocations Japan, so still there's… I mean… physical connection between the processing span and the lambda invocation span, and also, still, they will be able to, see their lambda invocation performances, I mean, in the overall lambda function invocation performance. So, that was the reason that why I'm suggesting that by default, I mean, prefer the parent-child relation, at least for the processing spans, for the producer spends.
And then, as you suggested, that having a configuration to switch between two approaches, I mean, is okay to me.
**Tyler Benson** 28:17 Okay.
I missed it. Did you say you have a PR that makes this change?
That you want to propose?
**Serkan Özal** 28:28 No, no, I just, reviewed Warius PR, and also just checked the screenshots and the data, and as far as I see, and also he mentioned that this is not working in the New Relic, so what I am saying is that Doing these changes in the worries PR, if everyone is okay? I mean… configurable parent-child relation and the spelling approach, but by default, use the parent-child approach. So that's my, proposal.
in this PR.
**Tyler Benson** 29:04 Okay.
**Warre Pessers** 29:07 Yeah, also fine for me, … We'll look into, … updating the PR, then?
Anything else on the context propagation stuff, or not?
**Serkan Özal** 29:28 Nope. I'm okay with that, I mean, … Actually, there are multiple improvements in this PR. Basically, since we have the control over the creating individual spans for each SQS process message, that's okay, so we just need to find… find a way. I don't think it should be hard.
to… to have a configurable, I mean, linking, instead of file, or the… or the SPL linking, and then that's okay.
And once we complete and release this feature, maybe we can also talk about whether we can apply the similar approach for the other event types, like the SNS, for example, very similar to the SQS.
And maybe the other, trigger types?
maybe the Kinesis, for example, I don't know. Maybe the S3, but I think S3, it is… it's… I mean… needs to be, handled over the X-ray, because there's no… through context propagation over the S3, but I think we can apply the similar and same approach, actually, not the similar, the same approach to the SNS, I believe.
**Warre Pessers** 30:44 Yup.
I think so, too.
… I did have some other things to discuss, so there was also… an open issue about, Python instrumentation, someone asking for more Python instrumentation. This is a little bit familiar to me, as this sort of issue for Node.js was the first.
thing I actually, got involved with here, so I will be looking into the effects on layer size and cold starts of adding more instrumentation for the Python layers, and we'll do some testing to see if it's actually viable.
… And then there was one more thing I wanted to discuss, but this is actually a little bit of, overlap with Maxime's, actual day-to-day job, because he, … proposed some sort of change to no longer support callback-style lambda handlers, … on the AWS side, sorry. And I noticed in the lambdas at my workplace that, this… Apparently, using the Lambda instrumentation in the Lambda layers actually, produces some warning logs related to this, because the Lambda instrumentation behind the scenes, turns any Lambda handler into a callback-style lambda handler, when it gets patched for, OpenTelemetry instrumentation, so… that will definitely be something we need to look into, but I can also… ping Max in the Slack channel, to discuss with him.
**Tyler Benson** 32:38 Yeah, that definitely sounds concerning, and thank you for being on top of that.
**Warre Pessers** 32:42 Yeah, it would only be an issue, if you actually, upgrade to Node.js 24 when that releases, but, yeah, something to be aware of.
**Tyler Benson** 32:54 Okay.
Great.
Well, nice meeting today, everyone. Was there anything else?
**Serkan Özal** 33:06 Nope, from my side.
**Warre Pessers** 33:08 Also, not from my side.
**Tyler Benson** 33:11 Cool. Well, James, thanks for joining us today.
**James Thompson** 33:14 That's alright.
**Serkan Özal** 33:15 Yep, thank you, everyone. Thank you, James. Nice to meet you, and have a good day.
**Tyler Benson** 33:21 Cheers. Bye.
**Warre Pessers** 33:22 But….
