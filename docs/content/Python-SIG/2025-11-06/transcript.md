SIG: Python SIG
Date: 2025-11-06
Duration: 24 minutes
Zoom Recording URL: https://zoom.us/rec/share/NYFPQ2ibg9QAoyxxmuiMbNIVXK4c7vb2wVBk2XffFaQ-euhTDXrNqCCkR5T6-jxJ.dV_YVIrXfoFZhLPv
============================================================

## Zoom Recording Transcript

**Riccardo Magliocchetti** 02:45 Hello.
**Bhaskar Banerjee** 02:49 None.
**Riccardo Magliocchetti** 03:51 So welcome, everyone, to this, week Python sequel. We're going to wait a few more minutes for more people to join. In the meantime, please add yourself as an attendee.
To the sign notes. And also, if you have any last-minute topic you want to discuss.
Please add them to the notes as well.
And I shared the link to the NOS document in the chat.
**Bhaskar Banerjee** 04:18 Thank you, Ricardo.
Andrew and I are from Capital One and from our enterprise. We don't have access to this doc.
That is why I've added our concern or question in the chat.
Would you be okay to pick it up from chat and add it here as another thing to discuss?
**Riccardo Magliocchetti** 04:44 But, like, do you get an error assessing the dock?
**Bhaskar Banerjee** 04:49 Sorry, we can't access the dock from our enterprise, it is…
**Riccardo Magliocchetti** 04:54 Okay, okay, so it's Company Place, okay.
**Bhaskar Banerjee** 04:57 Depending upon this.
**Riccardo Magliocchetti** 04:59 I'm ready, I'm editing it for you.
Thank you.
**Bhaskar Banerjee** 05:02 Thank you so much.
I've supplemented the documentation that I was referring to.
If you could add that.
That shit one.
Thank you so much.
**Aaron Abbott** 05:52 Hey everyone, how's it going?
**Emídio** 05:56 Blue.
**Aaron Abbott** 06:03 Please add your names to the attendees, if you have a chance.
And, any topics?
**Riccardo Magliocchetti** 06:21 Yeah, like, we were waiting for more people to join, thanks.
**Aaron Abbott** 06:26 Yeah.
**Riccardo Magliocchetti** 06:36 Okay, it's a 5, so I think we can start.
So, yeah, again, please add yourself as an attendee.
And… The first topic?
It's from me, a quick one.
Yeah, like, take a look at the actual PRs.
And… yeah, like, oh, okay.
And, yeah, I tried to run PyRite on the logs code, and we have some warnings about, like.
Some confusion about types.
So, yeah, actually, if you have time, please take a look at this.
And, like, it would be nice to, like, enable pyrite.
On the code, so at least we check it.
**Hector Hernandez** 07:28 Yeah, thank you very much for Rubio and Ricardo. I will take a look at it today. Thank you.
**Riccardo Magliocchetti** 07:34 Thank you.
And… okay.
Next topic from Bhaskar on Hotelp Standard Out Export in JSON format.
**Bhaskar Banerjee** 07:51 John? Good morning, everyone. Good afternoon.
This is Andrea and Baskar. We are at Capital One.
And we have been exploring Different options available for… the exporters.
I see that if you open the context, Ricardo?
I've pasted the context where a new exporter has been made available.
It is the OTLP STD out.
Similar to console.
and this is already available in Java, in experimental phase.
And it's sending out the metrics, traces, and logs in a JSON format.
I see there is a PR open for this.
For the logs piece.
OTLP JSON Logs Explorer.
for Python. I'll share the link here.
I wanted to know if there are plans for this.
To be extended to metrics and traces.
And if not, would you all be open If we raise an issue, And contribute to it.
We are especially looking Do a solution like this.
Because… are Lambda platforms.
Are suffering significantly when trying the traditional OTLP, HTTP, or OTLPGRPC route, and it's trying to figure out
Seeing this new exporter, trying to figure out if something of this sort can work out in Python.
That's our question here.
Open to you all.
**Riccardo Magliocchetti** 09:50 Yeah, like, I remember,
Like, Chris, opening this issue, and me answering.
And I think we discussed this some times ago.
And the issues were that we would like to have… Protoba 3… JSON Exporter?
But, but, you know, adding a new exporter will be, like.
Like, someone who should look after that code.
**Bhaskar Banerjee** 10:25 I'm okay to take that up. I don't have difficulty.
To maintain, contribute and maintain that. That's not a problem.
We are happy to contribute, but…
I'm not regular in the group.
So, I want to take feedback, opinion, concerns from you all who have been maintaining this.
Balog.
**Riccardo Magliocchetti** 10:45 like, if you've seen this comment, we already have, Daft PR. I think we have, two PRs. One is the regional one, and the reason… okay, this one is the one already on top.
Of the other.
And so… Like, for me, the first thing would be, like, to take a look at the comments.
At a base piece on top of latest code.
**Bhaskar Banerjee** 11:10 Okay.
**Riccardo Magliocchetti** 11:11 Yeah, start from there.
**Aaron Abbott** 11:14 Ricardo, why does this one say HTTP in the PR title?
**Bhaskar Banerjee** 11:18 Exactly. I was about to ask the same question.
If you scroll up, it says… even in the header, you say it says HTTP. So, little curious, why is it HTTP?
**Riccardo Magliocchetti** 11:34 Like, I think this one, add… is adding, acrylicer.
What is… serializing to JSON without going through protobuf?
**Bhaskar Banerjee** 11:49 Okay, so it's a JSON serializer being written to a file, or HTTP socket.
**Riccardo Magliocchetti** 11:55 Yeah, like, I think this is for HTTP, but I think this includes also the…
the JSOM per lie, or at least as the encoding part.
I think that was the…
**Bhaskar Banerjee** 12:11 No, I'm not falling. This is… this includes…
JSON encoding without going through protobuf?
**Riccardo Magliocchetti** 12:19 Yeah.
**Bhaskar Banerjee** 12:19 and… So, also sending JSON over HTTP, you are saying?
**Riccardo Magliocchetti** 12:27 Yeah, like… I think the interesting part is… We have an encoder.
**Bhaskar Banerjee** 12:34 Right?
**Riccardo Magliocchetti** 12:34 for each signal, and as far as I can see, it's… Does not depend on… on Protobuff stuff.
So…
**Bhaskar Banerjee** 12:46 This solves, like, I think.
**Riccardo Magliocchetti** 12:49 A couple more issues we have.
Oh… on other projects?
For example, like, this would help also,
usage of OpenTelemetry Python inside the operator, and also there is an OpenTelemetry injector project.
that it was willing to add Python support only if we have a product buff less.
And called the fall.
data.
**Bhaskar Banerjee** 13:20 For them to a day.
It is much more beyond the scope of simply.
**Riccardo Magliocchetti** 13:25 Yeah.
**Bhaskar Banerjee** 13:25 JSON format over console. Okay, got it.
Okay, let us take a look at this, and we'll come back to you.
**Riccardo Magliocchetti** 13:34 Yeah, like… Next meeting or something.
I think, like, maybe, like, you can skip the HTTP part?
**Bhaskar Banerjee** 13:41 But just, maybe just take a look at the…
**Riccardo Magliocchetti** 13:44 Protocol workflows, encoding.
**Bhaskar Banerjee** 13:47 Good.
But are you guys open… are you guys open to the concept of JSON over console?
as has been advertised in the spec. Is that idea open, or…
Are there concerns in that area?
**Aaron Abbott** 14:05 I mean, I'm definitely supportive of it. I think it's, A nice feature.
**Bhaskar Banerjee** 14:14 Alright. Thanks. Yeah, I specifically asked that because
When I look at the console exporter's documentation, it calls out as non-productionizable.
And inherently, it can break without heads up.
So, it does not send good vibes to people who are using it.
So I wanted to know from the maintainers.
As to what parts they have about it. That is why I asked this question.
**Aaron Abbott** 14:44 Yes, I mean, the other console format is not specified. I think that's the main reason. Agree, agree.
**Bhaskar Banerjee** 14:51 Totally, yeah, totally agree on that, totally agree on that.
So let's go over this, and, Ian Andrew will go over this, look at the…
Encoder, and look at what is it doing.
And, if possible.
If… so if we have to contribute, what is the model? Do we… so this hasn't been merged yet, it's been draft. Do we contribute back to this, or do we raise on top of this, create a branch of this?
What is the model we followed?
**Riccardo Magliocchetti** 15:24 I think since… I think this hasn't been updated in… Months?
I'd say, like, if you want to use some of the code.
I'd say, like, rebase on top of this, like, create a branch on top of this, but…
like, if you want to open a PR, just open a guest main, our main, instead of…
Other people' branches.
**Bhaskar Banerjee** 15:48 Sounds good. Thank you. That was all we had.
Back to you guys.
Thank you so much.
**Aaron Abbott** 15:54 Yeah, I think before moving on, I want to understand, Ricardo, like, the…
requirement to not use Bertabuff Library, is that… Super hard requirement, like, I'm…
We can dig into the issues, if I remember correctly.
One of the goals was to not have a dependency on native code.
**Riccardo Magliocchetti** 16:13 Yep, exactly that.
**Aaron Abbott** 16:16 Yeah, and the Protobuf Library is maybe a little…
a little bloated for serverless, so it increases the image size.
Is that… I mean, we already have some code here that's true.
But is that a hard requirement, still?
**Riccardo Magliocchetti** 16:33 Like, for me, it's not, but…
Like, it would be very nice to… You know, through…
To catch two birds with a stone while listening.
What did happen?
**Aaron Abbott** 16:55 Yeah, I agree, we already have this prototype, it seems nice, but I do think we should validate it.
with the protobuf implementation, at least in the test, just because I imagine if it's just a bunch of, you know, hard-coded strings, then it's gonna be a little bit difficult to,
To get what we want, so…
**Riccardo Magliocchetti** 17:16 Thank you so much.
Yep.
**Aaron Abbott** 17:21 Sorry, go ahead, Ricard.
**Riccardo Magliocchetti** 17:22 Like, I was just going to say that if you are going to reuse, a part of our current exporters and encoders.
Like, the implementation would be, like, trivial, because Portoval already has…
code to move from, encoded message to JSON, so…
**Aaron Abbott** 17:44 Yep.
**Bhaskar Banerjee** 17:45 what I hear is that one…
ask is not to use Protobuf, right?
**Aaron Abbott** 17:54 Correct, yeah.
**Riccardo Magliocchetti** 17:56 Like, if you can, it will be great, but yeah.
**Bhaskar Banerjee** 18:01 Sure. Yeah, let's… we will try for it.
**Aaron Abbott** 18:04 Okay, great. And one more ask on this, can you just… when you do this, can you just make sure that you enable, type checking, just from the start? I don't want to frustrate you by implementing the whole thing and then coming back with,
With that request, right?
**Bhaskar Banerjee** 18:19 of ship.
**Aaron Abbott** 18:20 Yeah, so you basically can add it to the py project file, there's, like, an allow list in the PyRite config, so please just do that for your early-ons to save frustration.
**Bhaskar Banerjee** 18:31 shouldn't.
Thank you, that's all from us.
**Aaron Abbott** 18:41 Thank you.
**Riccardo Magliocchetti** 18:43 Thank you.
And, yeah, it was the last topic for today. Anyone else?
Something else we want to discuss?
**Aaron Abbott** 19:12 No, not really,
I think, besides that one PR you shared, Ricardo, are we doing good on logs for the next release?
**Riccardo Magliocchetti** 19:20 Yeah, like, we are kind of blocked on… on getting the first pair merged.
**Aaron Abbott** 19:26 And then we have the other one on top of that.
**Riccardo Magliocchetti** 19:33 Yeah, like, I hope we can… Unblock this one,
I'm madvis.
Shortly.
**Aaron Abbott** 19:42 Okay.
Sounds good.
Thanks, everyone.
**Riccardo Magliocchetti** 19:49 Thanks, everyone. Thank you.
Environment?
**Emídio** 19:52 Thank you.
