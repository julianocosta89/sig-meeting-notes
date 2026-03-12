SIG: FAAS WG
Date: 2025-08-14
Duration: 27 minutes
============================================================

## Zoom Recording Transcript

**Serkan Özal** 02:51 Hello, good morning.
**Tyler Benson** 02:55 Hello! Good afternoon, evening.
**Serkan Özal** 02:58 Yeah, thank you.
Hello?
**Warre Pessers** 03:02 Hello.
**Serkan Özal** 03:04 I think we are just 3 of us.
Seems that I will not be able to join, or will be able to hear lately. So I think we can start.
And, … I don't have any, specific agenda, as there is no, I mean, recently reported critical issue, and also, I think we, … we should have a release by this week, because because it has passed about one month from the… since the previous release, and I think we are at a stable point to… to have a release. As of now, it's… I mean, if everyone is agreeing on that.
**Tyler Benson** 03:55 That sounds good to me. I think it's my turn this time, since you took the last one, so I'm happy to do that.
**Serkan Özal** 04:03 Okay, no problem, sure.
And yeah, I mean, as I said, I mean, I didn't see any critical issue report recently, so I don't have any issue to talk on, in this.
meeting, but also I have seen, Wari sent a draft version of, his works for the context propagation. So I will be, start reviewing the, the changes to, to understand the.
the solution, but as, I mean.
he already mentioned about the general approach, so I think I will be okay with the… with the overall approach. And, yeah, I mean, do you want to give some, some background info and details about your, your story?
**Warre Pessers** 04:54 Yeah, maybe, … let me think what could be interesting to show real quick. So basically, I have to see how to… share my screen properly here in Zoom.
Let's try… Just a second, I need to give it some permissions, apparently.
**Serkan Özal** 05:19 Yeah, I think you may need to restart the….
**Warre Pessers** 05:22 Yeah, okay, I'm back in a second.
**Tyler Benson** 05:35 Is there a link, Serkin, to the work he's doing that we should put in the agenda?
**Serkan Özal** 05:42 For the worries, PR, or…?
**Tyler Benson** 05:45 Rory, do you have a link to the work you've been doing that we can put in the agenda?
**Warre Pessers** 05:51 Yeah, ….
**Serkan Özal** 05:53 piv link here, just Kim Seven.
**Warre Pessers** 05:56 Okay.
Good. Let's… Let's see… So… this should work now… Okay, do you see my screen?
**Serkan Özal** 06:14 Yep.
**Warre Pessers** 06:15 Alright, so basically, it's not that big of a change. I don't know what this icon is doing. … basically the PubSub propagation utils, I looked into how this library works, and it does seem to me that this does everything that we require, of it, so I… added some… Pretty basic, codes to instrument those, … Array methods, … As you can see right here… There's also this, … context extractor for SQS, so that we can, get the actual context from the message attributes. That's a minor change. Let's… Just jump through… Kind of forgetting where this all is supposed to be, … This one right here.
… Alright… So, basically, what I did was, I checked if the incoming Lambda event contains records, which is only a thing if you, have an SQS event source mapping.
So then I just get the messages from the records, try to determine the queue, the source queue, and then it's just as simple as using the PubSub propagations patch method.
You then specify a couple of things, like the parent context, which you have, tracer, which you also have here, and then the way that your Message gets, … It's spend details extracted. … So, yeah, that's why we use the SQS context getter, to actually get it from the message attributes. This is something we get from the trace context, property that should be present if you use the W3C propagator.
And then basically that's it. So, this will do everything for you. I did add some tests, because I think maybe my explanation is not that clear, but the tests should make this a bit, … easier to understand, I think.
… let's… C….
**Tyler Benson** 09:09 Quick question. Is this similar in… in spirit to, what, the… what I showed you a while back around what Java was doing?
**Warre Pessers** 09:19 Well, a little bit. The thing is, so, in Java, there was a lot of helpful stuff you have, and builders to build your span links, which were then used in turn by that specific SQS handler, if I recall correctly.
And then the support for this in Node is a little bit different, but that's when I said a couple of weeks ago.
I already mentioned something about this PubSub propagation package, which is also just something that, is maintained here in the JSConstrip rep repo, which is already….
**Tyler Benson** 09:58 I'm talking specifically around in terms of, like, the specific mechanics for interacting with the AWS API.
Or the SDK.
So is it basically doing the same thing where, you're… you're passing along, the… The propagation, as attributes.
**Warre Pessers** 10:22 Yeah, exactly. That's what I was… trying to show… I think this should be way more clear if I show you my test, but that's exactly what it does.
Okay.
**Serkan Özal** 10:39 Actually, sorry for interrupting, Rory. I have a few quick questions, so far.
**Warre Pessers** 10:45 Yeah. Yeah, the first one is that, as far… I mean….
**Serkan Özal** 10:48 Are you handling the, spam linking?
you know, I'm in the current implementation, or just the SQS processing, CPANS points to the… the propagated context?
**Warre Pessers** 11:05 Yeah, the second thing you mentioned, so the… the PubSub propagation now takes care of creating spam links, and those link back to the context that was propagated, in your message attributes.
**Serkan Özal** 11:24 Okay, so… Do we still have the overall evocation span?
**Warre Pessers** 11:32 The Lambda invocation spend? Yeah, we do.
**Serkan Özal** 11:35 Okay.
So… so in that case.
… I mean, how the hierarchy between the spans will be, like… like, let's say that the parent context span, and under the parent context span, do we still have the lambda imbocation span?
**Warre Pessers** 11:54 Yes, I have a small example here, which was only one SQS message, but, … these are the spans, and you can see this span is just your lambda invocation span. I'm not going to expand on all the properties, but that's basically just the lambda invocation span. You also see it doesn't have a parent span context. And then here, you have your, … Processing span, I think… Wait, let's see, I maybe have it backwards… No, no, … yeah, this is your lambda invocation span, indeed. And then here is your processing span, which has, of course, as parent, is your lambda invocation span. And then there's some span links in here, which link back to the original producer span.
**Serkan Özal** 12:53 Okay. So the processing span still points to the lambda implocation span, but they have also linked to the producer, span, right?
**Warre Pessers** 13:03 Yep, exactly. So, they… link, as in their parent span context is set to that lambda invocation span, so that's, like, your standard collapsible view of parent-child spans. This is just a child span of the lambda invocation span.
And then it has a spanned link to… the producer spend.
Is that clear?
**Serkan Özal** 13:32 I think I got it. Can you also share this JSON file? So… or… and also, if you have… I mean… Had a chance to export these trace to a tracing backend, so you can see participants visually.
**Warre Pessers** 13:52 Yeah, definitely, I'll, I'll do that, after today. And then maybe let's real quick… so, this is the way I structured the event. I dropped some properties that we don't require, so I only, took the relevant stuff here, so message attributes, which have those trace parent stuff.
then event source and event source ARN, so that you can extract the queue name from this, and then this should probably clarify some things, I think, also for what Tyler asked a second ago.
So, yeah, basic assert, this one is maybe a little bit redundant, but we check that there are two spans actually exported in memory. Then we check that the… It's also maybe a little bit verbose, I don't know, but that the first span that is exported has a parent span context that is the same trace ID as that second span, so that second span is your lambda invocation span.
And then here we do the same thing, but for the span ID, and then in the end, we also check that the links to that propagated context are present. So, I don't know if this is all clear enough to both of you?
**Serkan Özal** 15:09 Yeah, actually, I have, my another, I mean, quick feedback is that while deciding whether the event is a really SPS event or not.
It might be safer to look at some other properties, not just the records property. Yeah. Like, for example, checking the, event source.
property of the first element in the records array, maybe, that might be, safer to decide whether the event is really a SQLS event or not, because, I mean.
Not sure whether the records property is available in another Lambda event, but just looking at the single records property seems a little bit, I mean, fragile to me, just to decide whether it is … a space event or not.
**Warre Pessers** 16:01 Yeah, yeah.
**Serkan Özal** 16:02 My second, question is that… Not sure whether, I mean, mmm… … I mean, how many, tracing backends support the… Trace linking. So let's say that we have individual recipients for each processing SPS message, and then they have links to the producer site.
So that's good. But, for example, had you a chance to… to try with, sorry, example, like, the, the Grafana, or, Zipkin, or… or Yaya?
or Honeycomb.
**Warre Pessers** 16:42 Yeah, so I personally use Grafana for testing most of the tracing stuff, but I haven't had a chance yet to actually, like, build my own version of this library and deploy it so I can see it working, but that was on my to-do list, next.
Or maybe, as you said, I can just import the traces, … manually, and then see how it looks, but I think we definitely want to try to actually build this… yeah, quickly build my own version of this library, and then deploy it to see it working. I think that's a good idea.
**Serkan Özal** 17:20 Yeah, yeah, my reason was that, I mean, actually, it is, I mean, when you have the same trace ID, for the whole flow, I mean, it is easy for the tracing backend to show all the things in the same view, but when there are links and links to links and links to links over the whole flow, it might be… I mean, … harder for the tracing backend to show all the things in a single page, and… I even not sure whether, I mean, how many of the tracing vendor tracing backend tracing vendors support this. So, I mean, like, when you are querying the participants to have the trace map in a single view by the trace ID, Whether they are automatically collecting the other recipients, link it to those.
**Warre Pessers** 18:10 Cpas in that trace.
**Serkan Özal** 18:12 So that's just my, my worry about whether the tracing packets… I mean, the majority of the tracing packets will really support of that or not, because, I mean, depending on, I mean, how many of them support this.
We may need to change the trace linking approach. I mean, maybe we can just have the individual processing spans in the same trace with the producer side, but just linked to the invocation span.
That's just an idea, but as I said, that depends on the… mostly depends on the tracing backend capabilities on trace linking.
**Warre Pessers** 18:56 Yeah, it makes sense. I do know that in Grafana, when I tried this out, not with Lambda, but just with ECS, the span linking did look good to me, but I'll definitely test this in Grafana, and then, … I guess it's best to also test some other providers, as you said, to see if most support it or not.
Sounds good.
**Serkan Özal** 19:28 okay, I mean, in overall, I like the approach, especially, as I said before, I really find it interesting in patching the array methods.
That's… that's a really cool idea, and… yeah.
Thank you for your efforts, Rory.
**Warre Pessers** 19:46 Yeah, definitely, that's indeed… is a small consideration, though, that if, let's see… … Where was this? So the… Yeah, I can't navigate, it's here. Because we patched the array methods, you can't just do a normal for loop over your event records. You do have to call an array method like forEach, or map, or, ….
**Serkan Özal** 20:13 Croft, like… Yeah, okay, I see.
**Warre Pessers** 20:16 But, yeah, I guess that's just a limitation of, … Instrumentation, but should be okay, in my opinion.
**Serkan Özal** 20:25 Yeah.
**Warre Pessers** 20:29 Cool, nothing else about this? Tyler, was this clear for you as well?
**Tyler Benson** 20:35 I think so. I mean, as long as it, aligns with, the expectations of what the, the other languages are doing, like Java, for example, I think I'm good with it.
**Warre Pessers** 20:51 Yeah, I based this also on the semantic conventions. There's a page about, like, how the processing spans are supposed to… work exactly, and these do seem to come forward.
**Tyler Benson** 21:04 the main thing.
As long as it's the semantic conventions, it's great.
**Warre Pessers** 21:08 Okay.
Cool. Then I'll stop sharing now, unless, you want to see something else, but I don't think there's anything else, … Interesting to show about this.
Also, Ivan was, … also saying some things in the Slack thread, but he was experimenting with pulling his traces from X-ray, it seemed, and I don't think that it's necessarily relevant for this issue.
Because the way I see it is we just want to keep this all, … non-X-ray dependent, right?
**Serkan Özal** 21:58 Yeah, I mean, as far as I read the chat between you and I, Ivan, Ivan is mentioning about the SNS to SQS fanart, so basically the producer sends a message to SNS, and then SNS automatically publishes to the SQS queue, and then… lambda guest message from the SQSQ and process the message. In this flow, the SDK is on the producer side, so the SDK is able to trace to the SNS, and also on the consumer side, the SDK also is able to trace the receive message from SQL, that's okay, but the SNSQLS part is missing, because that happens in the background, and… that happens in the background on AWS, and we don't have, I mean, access to that part. There might be some workarounds later, not in this issue, because when the message is wrapped as SQS message to send to the SQS queue.
The… there are also some properties in the original message, the original SNS topic message, like the timestamp and the other attributes. So, it's like when you get a message from SQS to understand whether there is any SNS fanout or not, … there might be also additional, parsing based on the SPS message body to… to get the additional, information if the message itself is, I mean, forwarded through the SNS.
But that's it… but I don't think it will… I mean, it should be done in this effort. We can… we can also check those… those things later, whether we can do something or not.
From the X-ray perspective, as they are, I mean, able to see all parts of the AWS infrastructure, so it might not be hard for them, but from our side, we don't have any visibility between SNS and the SQS itself.
So, I think it is very expected that there might be some missing traces.
We have, but the AWS X-Ray has, because, I mean, they have all kinds of visibility on the AWS.
But yeah, I mean, in overall, I agree that I think we can address it later, but not in this issue, just to keep the… keep the context.
I mean, not complicated in this issue, just focus on the SQS directly SQS propagating over SQS should be fine.
At least for me.
**Warre Pessers** 24:48 Yeah, okay.
**Tyler Benson** 24:54 Yeah, I think from my perspective, the… excuse me… The main thing is that, when sending traces to X-ray.
Obviously, you're best off just to use, X-ray propagation and, the, active tracing to give you the best visibility. If you are trying to send to a third party, then if, collecting, integrating those active traces, active tracing spans into your trace, will lead to broken traces, unless you're doing, like, what Ivan does, and exporting the traces out from X-Ray into whatever third party you're using.
So, and that requires extra work, and I don't think is, like.
Easily supported, in, … I could be wrong, but I don't think it's easily supported. So, for third-party platforms.
I think the best option is to still use X-ray propagation.
So that we get the best, support for going across these other systems, like SNS and SQS.
… But ignoring the parent span, propag… the active tracing spans, that are presented in those environment variables.
**Warre Pessers** 26:31 Yeah, makes sense.
**Serkan Özal** 26:32 Yep.
**Tyler Benson** 26:34 So… I mean, you do lose a little bit of visibility from those active tracing spans, but, … I don't see a better option.
Other than just going back to X-Ray.
So… I think that's all I have.
**Warre Pessers** 27:02 Okay, … then I guess that's it for the SQS context propagation stuff. Was there anything else anyone wanted to discuss?
**Serkan Özal** 27:18 Nope, from my side.
**Tyler Benson** 27:20 Nope. I will, work on doing the releases, this week or next week.
When I find time.
**Serkan Özal** 27:28 Yeah, sure.
**Warre Pessers** 27:31 Okay.
**Tyler Benson** 27:32 Have a great day, everyone!
**Serkan Özal** 27:34 Everyone, take care. Bye-bye.
**Warre Pessers** 27:36 Bye-bye.
